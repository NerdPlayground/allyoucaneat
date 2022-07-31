import json
import requests
from orders.models import Order
from django.urls import reverse
from django.conf import settings
from products.models import Content
from django.contrib import messages
from customers.decorators import is_customer
from sasapay.authentication import get_client_token
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from sasapay.models import RequestPaymentResponse,PaymentProcessResult

def get_merchant_code(order):
    return order.product.vendor.till_number

def get_order(pk):
    return get_object_or_404(Order,pk=pk)

def get_error_message(data):
    error_response= str()
    for error_key,error_value in data.items():
        error_response += "%s: %s, " %(error_key,error_value)
    return error_response

@login_required(login_url="user:login")
@is_customer
def pay_order(request,pk):
    client_token= get_client_token()
    headers= {
        "Authorization": "Bearer %s" %client_token["access_token"]
    }

    order= get_order(pk)
    payload={
        "MerchantCode": get_merchant_code(order),
        "NetworkCode": settings.NETWORK_CODE,
        "PhoneNumber": request.user.phone_number,
        "TransactionDesc": "Pay for %s" %(order.product.name),
        "AccountReference": str(order.id),
        "Currency": settings.CURRENCY,
        "Amount": order.price.value,
        "CallBackURL": settings.CALLBACK_URL
    }

    response= requests.post(
        settings.PAYMENT_REQUEST,
        headers= headers,
        json= payload
    )
    
    data= json.loads(response.text)
    if response.status_code == 200:
        request_payment_response= RequestPaymentResponse(
            status= data.get("status"),
            detail= data.get("detail"),
            PaymentGateway= data.get("PaymentGateway"),
            MerchantRequestID= data.get("MerchantRequestID"),
            CheckoutRequestID= data.get("CheckoutRequestID"),
            ResponseCode= data.get("ResponseCode"),
            ResponseDescription= data.get("ResponseDescription"),
            CustomerMessage= data.get("CustomerMessage")
        )
        request_payment_response.save()
        return HttpResponseRedirect(reverse("sasapay:complete-payment",args=(order.id,)))
    else:
        data["Error Section"]= "Payment Request"
        return HttpResponse(get_error_message(data))

@login_required(login_url="user:login")
@is_customer
def complete_payment(request,pk):
    order= get_order(pk)
    context= {}
    if request.method == "POST":
        request_payment_response= RequestPaymentResponse.objects.get(
            MerchantRequestID= str(order.id),
        )

        client_token= get_client_token()
        headers= {
            "Authorization": "Bearer %s" %client_token["access_token"]
        }

        payload= {
            "CheckoutRequestID": request_payment_response.CheckoutRequestID,
            "MerchantCode": get_merchant_code(order),
            "VerificationCode": request.POST.get("verification-code"),
        }

        response= requests.post(
            settings.PROCESS_PAYMENT,
            headers= headers,
            json= payload
        )

        data= json.loads(response.text)
        if response.status_code == 200:
            order.paid= True
            order.save()
            return HttpResponseRedirect(reverse("customers:track-orders"))
        else:
            data["Error Section"]= "Process Payment"
            return HttpResponse(get_error_message(data))
    return render(request,"orders/pay_order.html",context)

def payment_process_results(request):
    data= request.data
    results= PaymentProcessResult.objects.create(
        MerchantRequestID= data.get("MerchantRequestID"),
        CheckoutRequestID= data.get("CheckoutRequestID"),
        ResultCode= data.get("ResultCode"),
        ResultDesc= data.get("ResultDesc"),
        TransAmount= data.get("TransAmount"),
        BillRefNumber= data.get("BillRefNumber"),
        TransactionDate= data.get("TransactionDate"),
        CustomerMobile= data.get("CustomerMobile")
    )
    results.save()