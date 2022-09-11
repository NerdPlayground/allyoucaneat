from math import prod
from django.db.models import Q
from django.urls import reverse
from orders.models import Order
from vendors.models import Vendor
from django.contrib import messages
from products.decorators import is_vendor
from customers.decorators import is_customer
from products.models import Product,Price,Content
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

def get_this_object(object_class,pk):
    return get_object_or_404(object_class,pk=pk)

def set_product_details(request,product):
    form_contents= request.POST.getlist("new-product-content-value")
    for form_content in form_contents:
        content= Content.objects.create(
            name=form_content,
            product=product
        )
        content.save()
    
    form_price_types= request.POST.getlist("new-product-price-type")
    form_prices= request.POST.getlist("new-product-price-value")
    for c in range(len(form_price_types)):
        price= Price.objects.create(
            type= form_price_types[c],
            value= int(form_prices[c]),
            product= product
        )
        price.save()

def get_product_catalogue(products):
    catalogue= dict()
    for product in products:
        contents= Content.objects.filter(product=product)
        product_contents= dict()
        for c in range(len(contents)):
            product_contents[c]= contents[c]
        
        prices= Price.objects.filter(product=product)
        product_prices= dict()
        for c in range(len(prices)):
            product_prices[c]= prices[c]

        catalogue[product]= [
            product_contents,product_prices
        ]
    return catalogue

@login_required(login_url="user:login")
@is_vendor
def my_shop(request):
    vendor= Vendor.objects.get(id=request.user.id)
    products= Product.objects.filter(vendor=vendor)
    context= {"catalogue":get_product_catalogue(products)}
    return render(request,"products/my_shop.html",context)

@login_required(login_url="user:login")
@is_vendor
def add_product(request):
    if request.method == 'POST':
        vendor= Vendor.objects.get(id=request.user.id)
        product_name= request.POST.get("product-name")
        product= Product.objects.create(
            vendor=vendor,
            name=product_name,
        )
        product.save()
        print()
        print(request.POST)
        print()
        set_product_details(request,product)
        return HttpResponseRedirect(reverse("products:my-shop"))
    context= {}
    return render(request,"products/add_product.html",context)

@login_required(login_url="user:login")
@is_vendor
def edit_product(request,pk):
    vendor= Vendor.objects.get(id=request.user.id)
    product= get_this_object(Product,pk)
    if vendor != product.vendor:
        return HttpResponse("You are not allowed to access this page")
    if request.method == "POST":
        product.name= request.POST.get("edit-product-name")
        product.save()
        set_product_details(request,product)
        return HttpResponseRedirect(reverse("products:my-shop"))
    context= {"product":product}
    return render(request,"products/edit_product.html",context)

@login_required(login_url="user:login")
@is_vendor
def delete_product(request,pk):
    vendor= Vendor.objects.get(id=request.user.id)
    product= get_this_object(Product,pk)
    if vendor != product.vendor:
        return HttpResponse("You are not allowed to access this page")
    if request.method == "POST":
        product.delete()
        return HttpResponseRedirect(reverse("products:my-shop"))
    context= {"obj":product}
    return render(request,"delete.html",context)

@login_required(login_url="user:login")
@is_vendor
def edit_product_group(request):
    if request.method == "POST":
        product_group_value= request.POST.get('product-group-values')
        edit_button= request.POST.get('edit-product-group-button')
        delete_button= request.POST.get('delete-product-group-button')
        if edit_button != None and delete_button == None:
            try:
                url_name= "products:edit-content"
                product_object= Content.objects.get(id=product_group_value)
            except Content.DoesNotExist:
                url_name= "products:edit-price"
                product_object= Price.objects.get(id=product_group_value)
        elif delete_button != None and edit_button == None:
            try:
                url_name= "products:delete-content"
                product_object= Content.objects.get(id=product_group_value)
            except Content.DoesNotExist:
                url_name= "products:delete-price"
                product_object= Price.objects.get(id=product_group_value)
        return HttpResponseRedirect(reverse(url_name,args=(product_object.id,)))

@login_required(login_url="user:login")
@is_vendor
def edit_content(request,pk):
    vendor= Vendor.objects.get(id=request.user.id)
    content= get_this_object(Content,pk)
    if vendor != content.product.vendor:
        return HttpResponse("You are not allowed to access this page")
    if request.method == "POST":
        content.name= request.POST.get("edit-content-name")
        content.save()
        return HttpResponseRedirect(reverse("products:my-shop"))
    context= {"content":content}
    return render(request,"products/edit_content.html",context)

@login_required(login_url="user:login")
@is_vendor
def delete_content(request,pk):
    vendor= Vendor.objects.get(id=request.user.id)
    content= get_this_object(Content,pk)
    if vendor != content.product.vendor:
        return HttpResponse("You are not allowed to access this page")
    if request.method == "POST":
        content.delete()
        return HttpResponseRedirect(reverse("products:my-shop"))
    context= {"obj":content}
    return render(request,"delete.html",context)

@login_required(login_url="user:login")
@is_vendor
def edit_price(request,pk):
    vendor= Vendor.objects.get(id=request.user.id)
    price= get_this_object(Price,pk)
    if vendor != price.product.vendor:
        return HttpResponse("You are not allowed to access this page")
    if request.method == "POST":
        price.type= request.POST.get("edit-price-type")
        price.value= request.POST.get("edit-price")
        price.save()
        return HttpResponseRedirect(reverse("products:my-shop"))
    context= {"price":price}
    return render(request,"products/edit_price.html",context)

@login_required(login_url="user:login")
@is_vendor
def delete_price(request,pk):
    vendor= Vendor.objects.get(id=request.user.id)
    price= get_this_object(Price,pk)
    if vendor != price.product.vendor:
        return HttpResponse("You are not allowed to access this page")
    if request.method == "POST":
        price.delete()
        return HttpResponseRedirect(reverse("products:my-shop"))
    context= {"obj":price}
    return render(request,"delete.html",context)

@login_required(login_url="user:login")
@is_customer
def products(request):
    query= request.GET.get('search-query')
    search_query= query if query != None else ''
    products= Product.objects.filter(
        Q(name__icontains=search_query)
    )
    context= {"products":products}
    return render(request,"products/products.html",context)

@login_required(login_url="user:login")
@is_customer
def product_details(request,pk):
    product= get_this_object(Product,pk)
    product_details= get_product_catalogue([product])[product]
    product_contents= product_details[0]
    product_prices= product_details[1]
    selected_prices= request.POST.get("product-prices")
    selected_contents= request.POST.getlist("product-contents")

    if request.method == "POST":
        if product.name == "Fruit Juice":
            if len(selected_contents) < 1 or len(selected_contents) > 4:
                messages.error(
                    request,
                    "Error: Select at least one flavor" if len(selected_contents) < 1 
                    else "Error: The selected flavors exceed the maximum limit of 4"
                )
                return HttpResponseRedirect(reverse("products:product-details",args=(product.id,)))
                
        elif product.name == "Fruit Salad":
            if len(product_contents) - len(selected_contents) > 1:
                messages.error(request,"Error: The limit of contents to be removed is 1")
                return HttpResponseRedirect(reverse("products:product-details",args=(product.id,)))
        
        order= Order.objects.create(
            product= product,
            customer= request.user,
            price= Price.objects.get(id=selected_prices),
        )
        for content in selected_contents:
            order.contents.add(Content.objects.get(id=content))
        order.save()
        return HttpResponseRedirect(reverse("orders:confirm-order",args=(order.id,)))
    context= {
        "product":product,
        "product_contents":product_contents,
        "product_prices":product_prices,
    }
    return render(request,"products/product_details.html",context)