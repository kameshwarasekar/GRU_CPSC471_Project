from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from  django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
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


#---------------------------University----------------------------------

@api_view(['GET'])
def university_get(request):
    university = University.objects.all()
    serializer = UniversitySerializer(university, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def university_getspecific(request, pk):
    university = University.objects.get(name = pk)
    serializer = UniversitySerializer(university, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def university_post(request, format=None):
    serializer = UniversitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def university_put(request, pk):
    university = University.objects.get(name=pk)
    serializer = UniversitySerializer(instance = university, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def university_delete(request, pk):
    university = University.objects.get(name=pk)
    university.delete()
    return Response('Item successfully deleted')



#---------------------------Degree----------------------------------

@api_view(['GET'])
def degree_get(request):
    degree = Degree.objects.all()
    serializer = DegreeSerializer(degree, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def degree_getspecific(request, pk):
    degree = Degree.objects.get(name = pk)
    serializer = DegreeSerializer(degree, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def degree_post(request, format=None):
    serializer = DegreeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def degree_put(request, pk):
    degree = Degree.objects.get(name=pk)
    degree = DegreeSerializer(instance = degree, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def degree_delete(request, pk):
    degree = Degree.objects.get(name=pk)
    degree.delete()
    return Response('Item successfully deleted')

#---------------------------Provides----------------------------------

@api_view(['GET'])
def provides_get(request):
    provides = Provides.objects.all()
    serializer = ProvidesSerializer(provides, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def provides_getspecific(request, pk):
    provides = Provides.objects.get(provides_id = pk)
    serializer = ProvidesSerializer(provides, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def provides_post(request, format=None):
    serializer =ProvidesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def provides_put(request, pk):
    provides = Provides.objects.get(provides_id=pk)
    provides = ProvidesSerializer(instance = provides, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def provides_delete(request, pk):
    provides = Provides.objects.get(provides_id=pk)
    provides.delete()
    return Response('Item successfully deleted')


#---------------------------Faculty----------------------------------

@api_view(['GET'])
def faculty_get(request):
    faculty = Faculty.objects.all()
    serializer = FacultySerializer(faculty, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def faculty_getspecific(request, pk):
    faculty = Faculty.objects.get(faculty_id = pk)
    serializer = FacultySerializer(faculty, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def faculty_post(request, format=None):
    serializer = FacultySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def faculty_put(request, pk):
    faculty = Faculty.objects.get(faculty_id=pk)
    faculty = FacultySerializer(instance = faculty, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def faculty_delete(request, pk):
    faculty = Faculty.objects.get(faculty_id=pk)
    faculty.delete()
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
