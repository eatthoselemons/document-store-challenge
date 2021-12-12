from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)

class Folder(models.Model):
    folder_name = models.CharField(max_length=50)
    document = models.OneToOneField(
        Document,
        on_delete=models.CASCADE,
        primary_key=True
    )

class topic(models.Model):
    topic_name = models.CharField(max_length=100)
    documents = models.ManyToManyField(Document)
