from django.shortcuts import render
from .models import Professor, University, Ranking
from django.views import generic


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
