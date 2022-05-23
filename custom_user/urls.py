from django.urls import path
from custom_user.views import register,login,profile,edit_profile,logout

app_name= "custom_user"
urlpatterns= [
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    path("profile/",profile,name="profile"),
    path("edit-profile/",edit_profile,name="edit-profile"),
    path("logout/",logout,name="logout"),
]