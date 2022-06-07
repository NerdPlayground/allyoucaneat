from django.contrib import admin
from custom_user.models import User

class UserAdmin(admin.ModelAdmin):
    list_display= [
        "id","first_name","last_name",
        "email","phone_number","is_active","is_staff",
        "customer","sasapay_vendor","external_vendor"
    ]
    list_filter= [
        "is_active","is_staff","customer",
        "sasapay_vendor","external_vendor"
    ]
    search_fields= ["first_name","last_name","email","phone_number"]

    fieldsets=[
        ("Information",{"fields":["first_name","last_name","email","phone_number"]}),
        ("Status",{"fields":["is_active","is_staff","is_superuser"]}),
        ("Category",{"fields":["customer","sasapay_vendor","external_vendor"]}),
    ]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        return False

admin.site.register(User,UserAdmin)