from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core.files import File
from django.http import JsonResponse
import json
import os
from .models import Document
from .models import Topic
from .models import Folder

base_path = settings.LOCAL_FILE_DIR

class Upload(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        document_name = data.get('name')
        folder_name = data.get('folder')
        topics = data.get('topics')
        file = request.FILES.items().values()[0]

        folder = Folder.objects.get(folder_name=folder_name)
        if not folder:
            folder = Folder.objects.create(folder_name=folder_name)
            folder.save()

        document = Document(title=document_name,
                            folder=folder)

        for item in topics:
            topic = Topic.objects.get(name=item)
            if topic:
                document.topics.add(topic)
            else:
                topic = Topic.objects.create(name=item)
                topic.save()
                document.topics.add(topic)
        document.save()

        file_path_and_name = os.path.join(base_path,folder_name,document_name)

        with open(file_path_and_name, 'w') as f:
            my_file = File(f)
            my_file.write(file.read())


# Create your views here.
