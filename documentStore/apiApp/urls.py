from django.urls import path
from .views import Upload, AllTopics, SearchFolder, SearchTopic

urlpatterns = [
    path('upload-file/', Upload.as_view()),
    path('all-topics/', AllTopics.as_view()),
    path('search-folder/', SearchFolder.as_view()),
    path('search-topic/', SearchTopic.as_view())
]