from django.urls import path
from .views import Upload

urlpatterns = [
    path('upload-file/', Upload.as_view()),
]