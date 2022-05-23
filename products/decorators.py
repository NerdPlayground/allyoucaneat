from urllib import request
from django.http import HttpResponse

def is_admin(func):
    def inner(*args,**kwargs):
        request= args[0] or kwargs["request"]
        if not request.user.is_staff:
            return HttpResponse("You are not allowed to access this page")
        return func(*args,**kwargs)
    return inner