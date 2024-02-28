from django.conf import settings
from django.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location =  settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION