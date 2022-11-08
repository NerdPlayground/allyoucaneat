from datetime import datetime
from django.db.models import Q
from vendors.models import Vendor
from django.shortcuts import render
from receipts.models import Receipt
from django.core.paginator import Paginator
from django.utils.timezone import make_aware

def sort_content(request,user,Content):
    business_names= list()
    shops= Vendor.objects.all().values("business_name")
    for shop in shops:
        business_names.append(shop["business_name"])
    
    sort_form_shop= request.GET.get("sort-form-shop")
    filter_shop= (
        sort_form_shop if sort_form_shop != None
        and sort_form_shop != "all" else ""
    )

    sort_form_period= request.GET.get("sort-form-period")
    filter_period= (
        Q(created_on__date=datetime.date(datetime.today())) if sort_form_period == "today" else 
        Q(created_on__week=datetime.today().isocalendar()[1]) if sort_form_period == "this-week" else 
        Q(created_on__month=datetime.today().month) if sort_form_period == "this-month" else 
        Q(created_on__year=datetime.today().year) if sort_form_period == "this-year" else
        Q(created_on__range=(make_aware(datetime.min),make_aware(datetime.max)))
    )

    if user.customer:
        contents= Content.objects.filter(
            Q(shop__icontains=filter_shop),
            filter_period,
            customer=user
        ).order_by("-created_on")
    elif user.sasapay_vendor or user.external_vendor:
        contents= Content.objects.filter(
            Q(shop__icontains=filter_shop),
            filter_period,
            vendor=user
        ).order_by("-created_on")
    
    paginator= Paginator(contents,5)
    page_number= request.GET.get("page")
    page= paginator.get_page(page_number)
    context= {
        "page": page,
        "shops": business_names,
    }
    return context