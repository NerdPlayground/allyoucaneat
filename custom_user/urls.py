from django.urls import path
from custom_user.views import register,login,logout

app_name= "custom_user"
urlpatterns= [
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
]