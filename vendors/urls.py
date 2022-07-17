from django.urls import path
from vendors.views import (
    orders,receipts,modify_user,
    register_external_vendor,
    register_sasapay_vendor
)

app_name= "vendors"
urlpatterns= [
    path("register-external-vendor/",register_external_vendor,name="register-external-vendor"),
    path("register-sasapay-vendor/",register_sasapay_vendor,name="register-sasapay-vendor"),
    path("edit-profile/",modify_user,name="edit-profile"),
    path("customers-orders/",orders,name="customer-orders"),
    path("customers-receipts/",receipts,name="customer-receipts"),
]