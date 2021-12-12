from django.db import models

class Folder(models.Model):
    folder_name = models.CharField(max_length=50)

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

class Document(models.Model):
    title = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, default=1)
    topics = models.ManyToManyField(Topic)
