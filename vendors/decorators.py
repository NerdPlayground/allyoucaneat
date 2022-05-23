from django.http import Http404,HttpResponse

def is_vendor(func):
    def inner(*args,**kwargs):
        request= args[0] or kwargs["request"]
        if not request.user.is_vendor:
            return HttpResponse("You are not allowed to access this page")
        return func(*args,**kwargs)
    return inner