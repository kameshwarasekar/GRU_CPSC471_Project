from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from  django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlumniSerializer, ProfessorSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.http import Http404
from rest_framework.decorators import api_view


# Create your views here.


# class AlumniList(APIView):
#     def get(self, request):
#         alumni = Alumni.objects.all()
#         serializer = AlumniSerializer(alumni, many=True)
#         return Response(serializer.data)


#---------------------------Alumni----------------------------------


@api_view(['GET'])
def alumni_get(request):
    alumni = Alumni.objects.all()
    serializer = AlumniSerializer(alumni, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def alumni_getspecific(request, pk):
    alumni = Alumni.objects.get(alumni_id = pk)
    serializer = AlumniSerializer(alumni, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def alumni_post(request, format=None):
    serializer = AlumniSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def alumni_put(request, pk):
    alumni = Alumni.objects.get(alumni_id=pk)
    serializer = AlumniSerializer(instance = alumni, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def alumni_delete(request, pk):
    alumni = Alumni.objects.get(alumni_id=pk)
    alumni.delete()
    return Response('Item successfully deleted')


#---------------------------Professor----------------------------------



@api_view(['GET'])
def professor_get(request):
    professor = Professor.objects.all()
    serializer = ProfessorSerializer(professor, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def professor_getspecific(request, pk):
    professor = Professor.objects.get(prof_id = pk)
    serializer = ProfessorSerializer(professor, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def professor_post(request, format=None):
    serializer = ProfessorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def professor_put(request, pk):
    professor = Professor.objects.get(prof_id=pk)
    serializer = ProfessorSerializer(instance = professor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def professor_delete(request, pk):
    professor = Professor.objects.get(prof_id=pk)
    professor.delete()
    return Response('Item successfully deleted')













# Create your views here.
def index(request):
    # num_prof = Professor.objects.all().count()
    # num_uni = University.objects.all().count()
    # num_course = Course.objects.all().count()
    # context = {
    #     'num_prof': num_prof,
    #     'num_uni': num_uni,
    #     'num_course': num_course
    # }
    return render(request, 'index.html')


def option(request):
    # num_prof = Professor.objects.all().count()
    # num_uni = University.objects.all().count()
    # num_course = Course.objects.all().count()
    # context = {
    #     'num_prof': num_prof,
    #     'num_uni': num_uni,
    #     'num_course': num_course
    # }
    return render(request, 'option.html')


class UniversityListView(generic.ListView):
    model = University


class UniversityDetailView(generic.DetailView):
    model = University


class ProfessorListView(generic.ListView):
    model = Professor


class ProfessorDetailView(generic.DetailView):
    model = Professor


class RankingListView(generic.ListView):
    model = Ranking


class RankingDetailView(generic.DetailView):
    model = Ranking
