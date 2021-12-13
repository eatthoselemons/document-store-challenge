from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core.files import File
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import os
from .models import Document
from .models import Topic
from .models import Folder

base_path = settings.LOCAL_FILE_DIR

@method_decorator(csrf_exempt, name='dispatch')
class Upload(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        document_name = data.get('name')
        folder_name = data.get('folder')
        topics = data.get('topics')

        try:
            folder = Folder.objects.get(folder_name=folder_name)
        except Folder.DoesNotExist as e:
            folder = Folder.objects.create(folder_name=folder_name)
            folder.save()

        try:
            document = Document.objects.get(title=document_name)
        except Document.DoesNotExist as e:
            document = Document(title=document_name,
                                folder=folder)
            document.save()

        for item in topics:
            try:
                topic = Topic.objects.get(topic_name=item)
                document.topics.add(topic)
            except Topic.DoesNotExist as e:
                topic = Topic.objects.create(topic_name=item)
                topic.save()
        document.topics.add(topic)
        document.save()

        data = {
            "message": f"new file added with name {document_name}"
        }
        return JsonResponse(data, status=201)


# Create your views here.
