from django.urls import path
from receipts.views import receipt

app_name="receipts"
urlpatterns= [
    path("receipt/<str:pk>/",receipt,name="receipt"),
]