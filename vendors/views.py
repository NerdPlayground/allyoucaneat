from orders.models import Order
from django.urls import reverse
from django.contrib import messages
from vendors.decorators import is_vendor
from django.http import Http404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

@login_required(login_url="user:login")
@is_vendor
def orders(request):
    context= {}
    return render(request,"vendors/orders.html",context)


@login_required(login_url="user:login")
@is_vendor
def receipts(request):
    context= {}
    return render(request,"vendors/receipts.html",context)