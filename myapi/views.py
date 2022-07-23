from urllib import response
from httplib2 import Response
import requests
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostsSerializer
from .models import Videos

class PostViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = PostsSerializer

def home(request):
    videos = Videos.objects.all()
    return render(request, 'myapi/home.html',context={'videos':videos})

@api_view(['GET'])
def getData(request):
    items = Videos.objects.all()
    serializer = PostsSerializer(items,many=True,context={'request': request})
    return Response(serializer.data)
