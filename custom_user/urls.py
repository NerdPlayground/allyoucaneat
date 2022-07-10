from django.urls import path
from custom_user.views import (
    roles,authenticate_user,
    profile,logout_user,delete_profile
)

app_name= "user"
urlpatterns= [
    path("roles/",roles,name="roles"),
    path("login/",authenticate_user,name="login"),
    path("profile/",profile,name="profile"),
    path("logout/",logout_user,name="logout"),
    path("delete-profile/",delete_profile,name="delete-profile"),
]