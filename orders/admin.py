from orders.models import Order
from django.contrib import admin
from products.models import Content
from django.utils.html import format_html_join

class OrderAdmin(admin.ModelAdmin):
    list_display= [
        "id","product","order_contents","order_price",
        "customer","paid","delivered","created_on"
    ]
    search_fields= ["customer"]
    list_filter= ["paid","delivered"]

    def order_price(self,obj):
        return obj.price.value

    def order_contents(self,obj):
        contents= Content.objects.filter(orders=obj.id).values_list("name")
        return format_html_join(
            '\n',"<li style='list-style-type:none;'>{}</li>",
            (content for content in contents)
        )
    
    fieldsets=[
        ("Order Information",{"fields":["product","order_contents","order_price"]}),
        ("Customer Information",{"fields":["customer","paid","delivered","created_on"]}),
    ]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        return False

    def has_delete_permission(self,request,obj=None):
        return True

admin.site.register(Order,OrderAdmin)