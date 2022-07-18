from django.contrib import admin
from django.utils.html import format_html_join
from products.models import Product,Content,Price

class ProductContent(admin.TabularInline):
    model= Content
    extra= 1

class ProductPrice(admin.TabularInline):
    model= Price
    extra= 1
    fields= ["type","value"]

class ProductAdmin(admin.ModelAdmin):
    list_display= [
        "id","vendor","name",
        "product_contents","product_prices"
    ]
    search_fields= ["name"]
    inlines= [ProductContent,ProductPrice]

    def product_contents(self,obj):
        contents= Content.objects.filter(product=obj).values_list("name")
        return format_html_join(
            '\n',"<li style='list-style-type:none;'>{}</li>",
            (content for content in contents)
        )

    def product_prices(self,obj):
        prices= Price.objects.filter(product=obj).order_by("value").values_list("value")
        return format_html_join(
            '\n',"<li style='list-style-type:none;'>{}</li>",
            (price for price in prices)
        )
    
    def has_add_permission(self,request):
        return False
    
    def has_change_permission(self,request,obj=None):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return True

admin.site.register(Product,ProductAdmin)