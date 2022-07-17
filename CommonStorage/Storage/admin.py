from django.contrib import admin
from .models import AWS, Azure, GCloud
# Register your models here.

admin.site.register(AWS)
admin.site.register(Azure)
admin.site.register(GCloud)