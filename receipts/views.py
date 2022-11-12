from django.urls import reverse
from django.contrib import messages
from receipts.models import Receipt
from customers.decorators import is_customer
from django.http import Http404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

@login_required(login_url="user:login")
def receipt(request,pk):
    receipt= Receipt.objects.get(id=pk)
    context={"receipt":receipt}
    return render(request,"receipts/receipt.html",context)