from django.contrib import admin
from customers.models import Customers

class CustomersAdmin(admin.ModelAdmin):
    list_display= [
        "id","first_name","last_name","email",
        "phone_number","is_active","is_staff","customer"
    ]
    list_filter= [
        "is_active","is_staff"
    ]
    search_fields= ["first_name","last_name","phone_number"]
    fieldsets=[
        ("Information",{"fields":["first_name","last_name","email","phone_number"]}),
        ("Status",{"fields":["is_active","is_staff","is_superuser"]}),
    ]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        return False

admin.site.register(Customers,CustomersAdmin)