from django.urls import path
from customers.views import (
    register_customer,receipts,
    track_orders,modify_user
)

app_name= "customers"
urlpatterns=[
    path("register-customer/",register_customer,name="register-customer"),
    path("edit-profile/",modify_user,name="edit-profile"),
    path("receipts/",receipts,name="receipts"),
    path("track-orders/",track_orders,name="track-orders")
]