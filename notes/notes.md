there is a method now in django 4.0 for reading in postgres passwords and configuration from a file but nothing for the secretkey that I know of so to keep things easier /more consistent will just keep the read json function for both
https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes




improvements:
use the `FileField` model from django
use HTTPS
use url parsing to change things to get requests

