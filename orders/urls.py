from django.urls import path
from orders.views import (
    confirm_order,pay_order,complete_payment,
    payment_process_results,delete_order
)

app_name= "orders"
urlpatterns= [
    path("confirm-order/<str:pk>/",confirm_order,name="confirm-order"),
    path("pay-order/<str:pk>/",pay_order,name="pay-order"),
    path("complete-payment/<str:pk>/",complete_payment,name="complete-payment"),
    path("payment-process-results/",payment_process_results,name="payment-process-results"),
    path("delete-order/<str:pk>/",delete_order,name="delete-order"),
]