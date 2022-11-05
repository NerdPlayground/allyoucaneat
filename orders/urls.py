from django.urls import path
from orders.views import (
    extra_instructions,
    confirm_order,delete_order,
)

app_name= "orders"
urlpatterns= [
    path("confirm-order/<str:pk>/",confirm_order,name="confirm-order"),
    path("delete-order/<str:pk>/",delete_order,name="delete-order"),
    path("extra-instructions/<str:pk>/",extra_instructions,name="extra-instructions"),
]