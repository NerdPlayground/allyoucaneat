from django.contrib import admin
from receipts.models import Receipt

class ReceiptAdmin(admin.ModelAdmin):
    list_display= [
        "id","order","customer","vendor",
        "paid","ready","created_on"
    ]
    search_fields= ["customer","order"]
    list_filter= ["paid","ready"]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request):
        return False

    def has_delete_permission(self,request):
        return False

admin.site.register(Receipt,ReceiptAdmin)