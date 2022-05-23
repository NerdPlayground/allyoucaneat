from django.urls import path
from orders.views import pay_order

urlpatterns= [
    path("pay-order/<str:pk>/",pay_order,name="pay-order")
]