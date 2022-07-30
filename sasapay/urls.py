from django.urls import path
from sasapay.views import (
    pay_order,complete_payment,
    payment_process_results
)

app_name= "sasapay"
urlpatterns= [
    path("pay-order/<str:pk>/",pay_order,name="pay-order"),
    path("complete-payment/<str:pk>/",complete_payment,name="complete-payment"),
    path("payment-process-results/",payment_process_results,name="payment-process-results"),
]