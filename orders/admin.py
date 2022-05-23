from orders.models import Order
from django.contrib import admin
from products.models import Content
from django.utils.html import format_html_join

class OrderAdmin(admin.ModelAdmin):
    list_display= [
        "id","product","order_contents",
        "customer","paid","created_on"
    ]
    search_fields= ["customer"]
    list_filter= ["paid"]

    def order_contents(self,obj):
        contents= Content.objects.filter(orders=obj.id)
        return format_html_join(
            '\n',"<li style='list-style-type:none;'>{}</li>",
            (content for content in contents)
        )

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request):
        return False

    def has_delete_permission(self,request):
        return False

admin.site.register(Order,OrderAdmin)