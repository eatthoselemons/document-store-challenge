there is a method now in django 4.0 for reading in postgres passwords and configuration from a file but nothing for the secretkey that I know of so to keep things easier /more consistent will just keep the read json function for both
https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes

the `ALLOWED_HOSTS` variable is a wildcard, is insecure



things for file:
import os
from django.conf import settings

def document_root():
    return os.path.join(settings.LOCAL_FILE_DIR, 'documents')


improvements:
use the `FileField` model from django
