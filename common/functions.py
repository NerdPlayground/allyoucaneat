from datetime import datetime
from django.db.models import Q
from vendors.models import Vendor
from receipts.models import Receipt
from feedback.models import Feedback
from django.core.paginator import Paginator
from django.utils.timezone import make_aware

previous_values=list()
def sort_content(request,user,Content):
    sort_form_shop= request.GET.get("sort-form-shop")
    sort_form_period= request.GET.get("sort-form-period")
    if sort_form_shop != None and sort_form_period != None:
        previous_values.clear()
        previous_values.append(sort_form_shop)
        previous_values.append(sort_form_period)
    elif len(previous_values) != 0:
        sort_form_shop= previous_values[0]
        sort_form_period= previous_values[1]

    filter_shop= Q(shop__icontains=sort_form_shop if sort_form_shop != None and sort_form_shop != "all" else "")
    filter_period= (
        Q(created_on__date=datetime.date(datetime.today())) if sort_form_period == "today" else 
        Q(created_on__week=datetime.today().isocalendar()[1]) if sort_form_period == "this-week" else 
        Q(created_on__month=datetime.today().month) if sort_form_period == "this-month" else 
        Q(created_on__year=datetime.today().year) if sort_form_period == "this-year" else
        Q(created_on__range=(make_aware(datetime.min),make_aware(datetime.max)))
    )

    if user.customer:
        contents= Content.objects.filter(
            filter_shop,
            filter_period,
            customer=user
        ).order_by("-created_on")
    elif user.sasapay_vendor or user.external_vendor:
        contents= Content.objects.filter(
            filter_shop,
            filter_period,
            vendor=user
        ).order_by("-created_on")
    
    paginator= Paginator(contents,5)
    page_number= request.GET.get("page")
    page= paginator.get_page(page_number)
    business_names= list()
    shops= Vendor.objects.all().values("business_name")
    for shop in shops:
        business_names.append(shop["business_name"])
    
    context= {
        "page": page,
        "shops": business_names,
    }
    return context