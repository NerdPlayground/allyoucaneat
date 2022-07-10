from django.urls import path
from customers.views import register_customer,orders,track_orders

app_name= "customers"
urlpatterns=[
    path("register-customer/",register_customer,name="register-customer"),
    path("all-orders/",orders,name="all-orders"),
    path("track-orders/",track_orders,name="track-orders")
]