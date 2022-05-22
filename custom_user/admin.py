from django.contrib import admin
from custom_user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= [
        "first_name","last_name","email",
        "is_active","is_staff","customer",
        "sasapay_vendor","external_vendor"
    ]
    list_filter= [
        "is_active","is_staff","customer",
        "sasapay_vendor","external_vendor"
    ]
    search_fields= ["first_name","last_name","email"]