from django.urls import path
from products.views import (
    products,all_products,add_product,
    edit_product,delete_product,prices,
    contents,add_content,edit_content,delete_content
)

urlpatterns= [
    path("",products,name="products"),
    path("all-products/",all_products,name="all-products"),
    path("add-product/",add_product,name="add-product"),
    path("edit-product/<str:pk>/",edit_product,name="edit-product"),
    path("delete-product/<str:pk>/",delete_product,name="delete-product"),
    path("prices/<str:pk>/",prices,name="prices"),
    path("contents/<str:pk>/",contents,name="contents"),
    path("add-content/",add_content,name="add-content"),
    path("edit-content/<str:pk>/",edit_content,name="edit-content"),
    path("delete-content/<str:pk>/",delete_content,name="delete-content"),
]