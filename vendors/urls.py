from django.urls import path
from vendors.views import orders,receipts

app_name= "vendors"
urlpatterns= [
    path("customers-orders/",orders,name="customer-orders"),
    path("customers-receipts/",receipts,name="customer-receipts"),
]