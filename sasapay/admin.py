from django.contrib import admin
from sasapay.models import RequestPaymentResponse,PaymentProcessResult

@admin.register(RequestPaymentResponse)
class RequestPaymentResponseAdmin(admin.ModelAdmin):
    list_display= [
        "id","status","detail","PaymentGateway","MerchantRequestID",
        "CheckoutRequestID","ResponseCode","ResponseDescription","CustomerMessage"
    ]
    search_fields= ["CheckoutRequestID"]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        return False

    def has_delete_permission(self,request,obj=None):
        return False

@admin.register(PaymentProcessResult)
class PaymentProcessResultAdmin(admin.ModelAdmin):
    list_display= [
        "id","MerchantRequestID","CheckoutRequestID","ResultCode",
        "ResultDesc","TransAmount","BillRefNumber","TransactionDate","CustomerMobile"
    ]
    search_fields= ["CheckoutRequestID"]

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        return False

    def has_delete_permission(self,request,obj=None):
        return False