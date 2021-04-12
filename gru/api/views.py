from django.shortcuts import render
from .models import Professor, University, Ranking
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'index.html')


def option(request):
    return render(request, 'option.html')


def profile(request):
    return render(request, 'profile.html')


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
