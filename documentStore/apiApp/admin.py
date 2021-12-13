from django.contrib import admin
from .models import Document
from .models import Topic
from .models import Folder

admin.site.register(Document)
admin.site.register(Topic)
admin.site.register(Folder)