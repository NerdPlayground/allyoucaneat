from django.urls import reverse
from django.contrib import messages
from products.decorators import is_admin
from customers.decorators import is_customer
from django.http import Http404,HttpResponse
from products.models import Product,Price,Content
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

@login_required(login_url="custom_user:login")
@is_customer
def products(request):
    products= Product.objects.all()
    context= {"products":products}
    return render(request,"products/products.html",context)

@login_required(login_url="custom_user:login")
@is_admin
def all_products(request):
    context= {}
    return render(request,"products/all_products.html",context)

def get_product(pk):
    return get_object_or_404(Product,pk=pk)

@login_required(login_url="custom_user:login")
@is_admin
def add_product(request):
    context= {}
    return render(request,"products/add_product.html",context)

@login_required(login_url="custom_user:login")
@is_admin
def edit_product(request,pk):
    context= {}
    return render(request,"products/edit_product.html",context)

@login_required(login_url="custom_user:login")
@is_admin
def delete_product(request,pk):
    context= {}
    return render(request,"delete.html",context)

@login_required(login_url="custom_user:login")
@is_customer
def prices(request,pk):
    product_prices= Price.objects.filter(product=get_product(pk))
    context= {"product_prices":product_prices}
    return render(request,"products/prices.html",context)

@login_required(login_url="custom_user:login")
@is_customer
def contents(request,pk):
    product_contents= Content.objects.filter(product=get_product(pk))
    context= {"product_contents":product_contents}
    return render(request,"products/contents.html",context)

@login_required(login_url="custom_user:login")
@is_admin
def add_content(request):
    context= {}
    return render(request,"products/add_content.html",context)

@login_required(login_url="custom_user:login")
@is_admin
def edit_content(request,pk):
    context= {}
    return render(request,"products/edit_content.html",context)

@login_required(login_url="custom_user:login")
@is_admin
def delete_content(request,pk):
    context= {}
    return render(request,"delete.html",context)