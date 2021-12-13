from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core.files import File
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import os
from .models import Document, Topic, Folder

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
            document = Document.objects.get(title=document_name,
                                            folder=folder)
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

@method_decorator(csrf_exempt, name='dispatch')
class All_Topics(View):
    def get(self, request):
        topics = Topic.objects.all()
        list_topics = []
        for item in topics:
            list_topics.append(item.topic_name)
        data = {
            "all topics": list_topics
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class Search_Folder(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        
        folders = Folder.object.filter(


@method_decorator(csrf_exempt, name='dispatch')
class Search_Topic(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
