from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display= ["id","customer","vendor","shop","created_on","receipt","content"]
    search_fields= ["receipt"]
    
    def has_add_permission(self,request):
        return False
    
    def has_change_permission(self,request,obj=None):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return True

admin.site.register(Feedback,FeedbackAdmin)