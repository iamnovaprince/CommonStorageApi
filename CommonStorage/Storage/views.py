from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from Storage.models import AWS as dbAws, Azure as dbAzure, GCloud as dbGCloud
from CommonStorage.settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY, AZURE_ACCOUNT_KEY, AZURE_ACCOUNT_NAME, GS_ACCESS_KEY_ID,GS_SECRET_ACCESS_KEY,GS_BUCKET_NAME
# Create your views here.

@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def AWS(request):
    if(len(AWS_SECRET_ACCESS_KEY) == 0 or len(AWS_SECRET_ACCESS_KEY) == 0 ):
        return Response("{PLease Provide AWS Credentails in Settings  to be able to upload to S3 Storage}")
    aws = dbAws.objects.filter(user=request.user)
    
    return Response(aws[0].file.url)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def Azure(request):
    if(len(AZURE_ACCOUNT_NAME) == 0 or len(AZURE_ACCOUNT_KEY) == 0 ):
        return Response("{PLease Provide Azure Credentails in Settings  to be able to upload to Blob Storage}")
    blob = dbAzure.objects.filter(user=request.user)
    
    return Response(blob[0].file.url)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def GCloud(request):
    if(len(GS_ACCESS_KEY_ID) == 0 or len(GS_BUCKET_NAME) == 0 or len(GS_SECRET_ACCESS_KEY) == 0 ):
        return Response("{PLease Provide Google Credentails in Settings to be able to upload to Cloud Storage}")
    gcloud = dbGCloud.objects.filter(user=request.user)
    
    return Response(gcloud[0].file.url)
    
#     return Response(aws[0].file.url)