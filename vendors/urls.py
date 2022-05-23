from django.urls import path
from vendors.views import orders,receipts

urlpatterns= [
    path("customers-orders/",orders,name="customer-orders"),
    path("customers-receipts/",receipts,name="customer-receipts"),
]