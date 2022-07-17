from django.db import models
from storages.backends.azure_storage import AzureStorage
from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.gcloud import GoogleCloudStorage
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class AWS(models.Model):
    file = models.FileField(storage= S3Boto3Storage() )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.file)
    
class Azure(models.Model):
    file = models.FileField(storage = AzureStorage() )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.file)
    
class GCloud(models.Model):
    file = models.FileField(storage= GoogleCloudStorage)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.file)
    


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)