from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core import serializers

from Storage.models import AWS as dbAws, Azure as dbAzure, GCloud as dbGCloud
from CommonStorage.settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY, AZURE_ACCOUNT_KEY, AZURE_ACCOUNT_NAME, GS_ACCESS_KEY_ID,GS_SECRET_ACCESS_KEY,GS_BUCKET_NAME
# Create your views here.

@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def AWS(request):
    file = request.FILES.get("file")
    if file:
        aws = dbAws(file=file,user=request.user)
        aws.save()
        return Response("File Saved")
    if(len(AWS_SECRET_ACCESS_KEY) == 0 or len(AWS_SECRET_ACCESS_KEY) == 0 ):
        return Response("{PLease Provide AWS Credentails in Settings  to be able to upload to S3 Storage}")
    
    aws = dbAws.objects.filter(user=request.user)
    data = []
    for f in aws:
        data.append(f.file.url)
    return Response(data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def Azure(request):
    file = request.FILES.get("file")
    if file:
        blob = dbAzure(file=file,user=request.user)
        blob.save()
        return Response("File Saved")
    if(len(AZURE_ACCOUNT_NAME) == 0 or len(AZURE_ACCOUNT_KEY) == 0 ):
        return Response("{PLease Provide Azure Credentails in Settings  to be able to upload to Blob Storage}")
    blob = dbAzure.objects.filter(user=request.user)
    data = []
    for f in blob:
        data.append(f.file.url)
    return Response(data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def GCloud(request):
    file = request.FILES.get("file")
    if file:
        gcloud = dbGCloud(file=file,user=request.user)
        gcloud.save()
        return Response("File Saved")
        
        
    if(len(GS_ACCESS_KEY_ID) == 0 or len(GS_BUCKET_NAME) == 0 or len(GS_SECRET_ACCESS_KEY) == 0 ):
        return Response("{PLease Provide Google Credentails in Settings to be able to upload to Cloud Storage}")
    gcloud = dbGCloud.objects.filter(user=request.user)
    data = []
    for f in gcloud:
        data.append(f.file.url)
    return Response(data)
    
#     return Response(aws[0].file.url)