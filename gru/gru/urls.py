"""gru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from api import views
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumni/', views.alumni_get, name = "alumni"),
    path('alumni/<str:pk>', views.alumni_getspecific, name = "alumni-specific"),
    path('alumni-create/', views.alumni_post,name ="alumni-create"),
    path('alumni-update/<str:pk>', views.alumni_put,name ="alumni-update"),
    path('alumni-delete/<str:pk>', views.alumni_delete,name ="alumni-delete"),

    path('professor/', views.professor_get, name = "professor"),
    path('professor/<str:pk>', views.professor_getspecific, name = "professor-specific"),
    path('professor-create/', views.professor_post,name ="professor-create"),
    path('professor-update/<str:pk>', views.professor_put,name ="professor-update"),
    path('professor-delete/<str:pk>', views.professor_delete,name ="professor-delete"),

    path('university/', views.university_get, name = "university"),
    path('university/<str:pk>', views.university_getspecific, name = "university-specific"),
    path('university-create/', views.university_post,name ="university-create"),
    path('university-update/<str:pk>', views.university_put,name ="university-update"),
    path('university-delete/<str:pk>', views.university_delete,name ="university-delete"),

    path('degree/', views.degree_get, name = "degree"),
    path('degree/<str:pk>', views.degree_getspecific, name = "degree-specific"),
    path('degree-create/', views.degree_post,name ="degree-create"),
    path('degree-update/<str:pk>', views.degree_put,name ="degree-update"),
    path('degree-delete/<str:pk>', views.degree_delete,name ="degree-delete"),

    path('provides/', views.provides_get, name = "provides"),
    path('provides/<str:pk>', views.provides_getspecific, name = "provides-specific"),
    path('provides-create/', views.provides_post,name ="provides-create"),
    path('provides-update/<str:pk>', views.provides_put,name ="provides-update"),
    path('provides-delete/<str:pk>', views.provides_delete,name ="provides-delete"),
    
    path('faculty/', views.faculty_get, name = "faculty"),
    path('faculty/<str:pk>', views.faculty_getspecific, name = "faculty-specific"),
    path('faculty-create/', views.faculty_post,name ="faculty-create"),
    path('faculty-update/<str:pk>', views.faculty_put,name ="faculty-update"),
    path('faculty-delete/<str:pk>', views.faculty_delete,name ="faculty-delete"),
    
    path('major/', views.major_get, name = "major"),
    path('major/<str:pk>', views.major_getspecific, name = "major-specific"),
    path('major-create/', views.major_post,name ="major-create"),
    path('major-update/<str:pk>', views.major_put,name ="major-update"),
    path('major-delete/<str:pk>', views.major_delete,name ="major-delete"),
    
    path('entryRequirement/', views.entryRequirement_get, name = "entryRequirement"),
    #path('entryRequirement/<str:pk>', views.entryRequirement_getspecific, name = "entryRequirement-specific"),
    path('entryRequirement-create/', views.entryRequirement_post,name ="entryRequirement-create"),
    # path('entryRequirement-update/<str:pk>', views.entryRequirement_put,name ="entryRequirement-update"),
    # path('entryRequirement-delete/<str:pk>', views.entryRequirement_delete,name ="entryRequirement-delete"),
    
    path('equivalentClass/', views.equivalentClass_get, name = "equivalentClass"),
    #path('equivalentClass/<str:pk>', views.equivalentClass_getspecific, name = "equivalentClass-specific"),
    path('equivalentClass-create/', views.equivalentClass_post,name ="equivalentClass-create"),
    # path('equivalentClass-update/<str:pk>', views.equivalentClass_put,name ="equivalentClass-update"),
    # path('equivalentClass-delete/<str:pk>', views.equivalentClass_delete,name ="equivalentClass-delete"),
    
    path('extraCurricularProgram/', views.extraCurricularProgram_get, name = "extraCurricularProgram"),
    path('extraCurricularProgram/<str:pk>', views.extraCurricularProgram_getspecific, name = "extraCurricularProgram-specific"),
    path('extraCurricularProgram-create/', views.extraCurricularProgram_post,name ="extraCurricularProgram-create"),
    path('extraCurricularProgram-update/<str:pk>', views.extraCurricularProgram_put,name ="extraCurricularProgram-update"),
    path('extraCurricularProgram-delete/<str:pk>', views.extraCurricularProgram_delete,name ="extraCurricularProgram-delete"),
    
    path('award/', views.award_get, name = "award"),
    #path('award/<str:pk>', views.award_getspecific, name = "award-specific"),
    path('award-create/', views.award_post,name ="award-create"),
    # path('award-update/<str:pk>', views.award_put,name ="award-update"),
    # path('award-delete/<str:pk>', views.award_delete,name ="award-delete"),
    
    path('extracurricularOfferings/', views.extracurricularOfferings_get, name = "extracurricularOfferings"),
    #path('extracurricularOfferings/<str:pk>', views.extracurricularOfferings_getspecific, name = "extracurricularOfferings-specific"),
    path('extracurricularOfferings-create/', views.extracurricularOfferings_post,name ="extracurricularOfferings-create"),
    # path('extracurricularOfferings-update/<str:pk>', views.extracurricularOfferings_put,name ="extracurricularOfferings-update"),
    # path('extracurricularOfferings-delete/<str:pk>', views.extracurricularOfferings_delete,name ="extracurricularOfferings-delete"),
    

]

urlpatterns += [
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('', RedirectView.as_view(url='api/', permanent=True)),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]