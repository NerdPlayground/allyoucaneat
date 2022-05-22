from django.urls import path
from customers.views import orders,track_orders

app_name= "customers"
urlpatterns=[
    path("all-orders/",orders,name="all-orders"),
    path("track-orders/",track_orders,name="track-orders")
]