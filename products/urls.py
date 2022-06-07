from django.urls import path
from products.views import (
    all_products,add_product,
    edit_product,delete_product,edit_content,delete_content,
    edit_price,delete_price,products,product_details
)


app_name= "products"
urlpatterns= [
    path("all-products/",all_products,name="all-products"),
    path("add-product/",add_product,name="add-product"),
    path("edit-product/<str:pk>/",edit_product,name="edit-product"),
    path("delete-product/<str:pk>/",delete_product,name="delete-product"),
    path("edit-content/<str:pk>/",edit_content,name="edit-content"),
    path("delete-content/<str:pk>/",delete_content,name="delete-content"),
    path("edit-price/<str:pk>/",edit_price,name="edit-price"),
    path("delete-price/<str:pk>/",delete_price,name="delete-price"),
    path("",products,name="products"),
    path("product-details/<str:pk>/",product_details,name="product-details"),
]