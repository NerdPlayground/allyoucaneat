from django.urls import path
from feedback.views import add_feedback,feedbacks,customer_feedbacks

app_name= "feedbacks"
urlpatterns= [
    path("add-feedback/<str:pk>/",add_feedback,name="add-feedback"),
    path("feedbacks/",feedbacks,name="feedbacks"),
    path("customer-feedbacks/",customer_feedbacks,name="customer-feedbacks"),
]