from django.urls import path
from products.views import products,prices,contents

urlpatterns= [
    path("",products,name="products"),
    path("prices/<str:pk>/",prices,name="prices"),
    path("contents/<str:pk>/",contents,name="contents"),
]