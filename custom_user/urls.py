from django.urls import path
from custom_user.views import (
    register,authenticate_user,
    profile,logout_user,delete_profile
)

app_name= "user"
urlpatterns= [
    path("register/",register,name="register"),
    path("login/",authenticate_user,name="login"),
    path("profile/",profile,name="profile"),
    path("logout/",logout_user,name="logout"),
    path("delete-profile/",delete_profile,name="delete-profile"),
]