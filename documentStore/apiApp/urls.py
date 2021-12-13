from django.urls import path
from .views import Upload, All_Topics, Search_Folder, Search_Topic

urlpatterns = [
    path('upload-file/', Upload.as_view()),
    path('all-topics/', All_Topics.as_view()),
    path('search-folder/', Search_Folder.as_view()),
    path('search-topic/', Search_Topic.as_view())
]