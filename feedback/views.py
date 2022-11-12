from django.urls import reverse
from django.contrib import messages
from receipts.models import Receipt
from feedback.models import Feedback
from customers.models import Customers
from vendors.decorators import is_vendor
from common.functions import sort_content
from customers.decorators import is_customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

@login_required(login_url="user:login")
@is_customer
def add_feedback(request,pk):
    if request.method == "POST":
        receipt= Receipt.objects.get(id=pk)
        customer= Customers.objects.get(id=request.user.id)
        feedback= Feedback.objects.create(
            customer=customer,
            receipt=receipt,
            vendor=receipt.vendor,
            shop=receipt.shop,
            content=request.POST.get("feedback")
        )
        feedback.save()
        return HttpResponseRedirect(reverse("feedbacks:feedbacks"))
    context={}
    return render(request,"feedback/add_feedback.html",context)

@login_required(login_url="user:login")
@is_customer
def feedbacks(request):
    customer= request.user
    context=sort_content(request,customer,Feedback)
    return render(request,"feedback/feedbacks.html",context)

@login_required(login_url="user:login")
@is_vendor
def customer_feedbacks(request):
    vendor=request.user
    context=sort_content(request,vendor,Feedback)
    return render(request,"feedback/feedbacks.html",context)