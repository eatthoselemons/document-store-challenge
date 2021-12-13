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
class AllTopics(View):
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
class SearchFolder(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        folder_to_search_for = data.get('folder')

        files = Document.objects.filter(folder__folder_name=folder_to_search_for)
        list_files = []
        for item in files:
            list_files.append(item.title)
        data = {
            "matching files": list_files
        }
        print(f"data: {data}")
        return JsonResponse(data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class SearchTopic(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        topic_to_search_for = data.get('topic')

        files = Document.objects.filter(topics__topic_name=topic_to_search_for)
        list_files = []
        for item in files:
            list_files.append(item.title)
        data = {
            "matching files": list_files
        }
        return JsonResponse(data, status=201)
