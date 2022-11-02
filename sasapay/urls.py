from django.urls import path
from sasapay.views import (
    pay_order,complete_payment,
    payment_process_results,
    transaction_status,
    verify_transaction,
)

app_name= "sasapay"
urlpatterns= [
    path("pay-order/<str:pk>/",pay_order,name="pay-order"),
    path("complete-payment/<str:pk>/",complete_payment,name="complete-payment"),
    path("transaction-status/<str:pk>/",transaction_status,name="transaction-status"),
    path("verify-transaction/<str:pk>/",verify_transaction,name="verify-transaction"),
    path("payment-process-results/",payment_process_results,name="payment-process-results"),
]