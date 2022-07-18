from django.contrib import admin
from vendors.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display= [
        "id","first_name","last_name","email",
        "phone_number","business_name","till_number",
        "is_active","sasapay_vendor","external_vendor"
    ]
    list_filter= [
        "is_active","is_staff",
        "sasapay_vendor","external_vendor"
    ]
    search_fields= [
        "first_name","last_name",
        "phone_number","till_number","business_name"
    ]
    fieldsets=[
        ("Information",{"fields":["first_name","last_name","email","phone_number"]}),
        ("Status",{"fields":["is_active","is_staff","is_superuser"]}),
        ("Role",{"fields":["sasapay_vendor","external_vendor"]}),
        ("Business",{"fields":["business_name","till_number"]})
    ]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return True

admin.site.register(Vendor,VendorAdmin)