from django.http import HttpResponse

def is_customer(func):
    def inner(*args, **kwargs):
        request= args[0] or kwargs["request"]
        if not request.user.customer:
            return HttpResponse("Warning: You are not allowed to view this page")
        return func(*args, **kwargs)
    return inner