from django.http import Http404,HttpResponse

def is_vendor(func):
    def inner(*args,**kwargs):
        request= args[0] or kwargs["request"]
        if request.user.sasapay_vendor or request.user.external_vendor:
            return func(*args,**kwargs)
        return HttpResponse("You are not allowed to access this page")
    return inner