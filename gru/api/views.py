from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alumni
from .serializers import AlumniSerializer

# Create your views here.


class AlumniList(APIView):
    def get(self, request):
        alumni = Alumni.objects.all()
        serializer = AlumniSerializer(alumni, many=True)
        return Response(serializer.data)
    def post(self):
        pass
