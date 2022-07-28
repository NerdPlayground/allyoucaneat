from django.contrib import admin
from receipts.models import Receipt

class ReceiptAdmin(admin.ModelAdmin):
    list_display= [
        "id","product_name","contents",
        "product_type","price","customer",
        "vendor","shop","created_on"
    ]
    search_fields= ["customer","vendor"]
    fieldsets= [
        ("Product Details",{"fields":[
            "product_name","contents","product_type","price"]}),
        ("Interaction Details",{"fields":[
            "customer","vendor","shop","created_on"]})
    ]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        return False

    def has_delete_permission(self,request,obj=None):
        return False

admin.site.register(Receipt,ReceiptAdmin)