from django.urls import reverse
from django.contrib import messages
from django.http import Http404,HttpResponse
from customers.decorators import is_customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

@login_required(login_url="custom_user:login")
@is_customer
def pay_order(request,pk):
    context= {}
    return render(request,"orders/pay_order.html",context)