from django.shortcuts import render
from .models import Professor, University, Ranking, Alumni
from django.views import generic
from django.http import HttpResponse
from  django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlumniSerializer, ProfessorSerializer

# Create your views here.


class AlumniList(APIView):
    def get(self, request):
        alumni = Alumni.objects.all()
        serializer = AlumniSerializer(alumni, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class ProfessorList(APIView):
    def get(self, request):
        professor = Professor.objects.all()
        serializer = ProfessorSerializer(professor, many=True)
        return Response(serializer.data)
    def post(self):
        pass

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
