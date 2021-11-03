from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.serializers import Serializer
from .serializers import SDSSerializer
from rest_framework.generics import ListAPIView

from sdsApp.models import SDS
from sdsApp.serializers import SDSSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sdsApp import serializers


# Create your views here.

class SDSApi(ListAPIView):
    queryset = SDS.objects.all()
    serializer_class = SDSSerializer
    def get_queryset(self):
        sdsdata = self.request.query_params
        print("here we are  ")
        print(sdsdata)
        print(" eend")

        return  SDS.objects.filter(folder=sdsdata['folder']).filter(topic=sdsdata['topic'])

@api_view(['GET'])
def apiOverview(request):
    api_urls={

        'Allrecords':'/Allrecords/'
    }

@api_view(['GET'])
def Allrecords(request):
    sdsData = SDS.objects.all()
    serializer = SDSSerializer(sdsData,many=True)
    return Response(serializer.data)







