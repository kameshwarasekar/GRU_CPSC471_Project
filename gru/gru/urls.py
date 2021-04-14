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
from api.views import profile



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
    path('entryRequirement/<str:pk>', views.entryRequirement_getspecific, name = "entryRequirement-specific"),
    path('entryRequirement-create/', views.entryRequirement_post,name ="entryRequirement-create"),
    path('entryRequirement-update/<str:pk>', views.entryRequirement_put,name ="entryRequirement-update"),
    path('entryRequirement-delete/<str:pk>', views.entryRequirement_delete,name ="entryRequirement-delete"),
    
    path('equivalentClass/', views.equivalentClass_get, name = "equivalentClass"),
    path('equivalentClass/<str:pk>', views.equivalentClass_getspecific, name = "equivalentClass-specific"),
    path('equivalentClass-create/', views.equivalentClass_post,name ="equivalentClass-create"),
    path('equivalentClass-update/<str:pk>', views.equivalentClass_put,name ="equivalentClass-update"),
    path('equivalentClass-delete/<str:pk>', views.equivalentClass_delete,name ="equivalentClass-delete"),
    
    path('extraCurricularProgram/', views.extraCurricularProgram_get, name = "extraCurricularProgram"),
    path('extraCurricularProgram/<str:pk>', views.extraCurricularProgram_getspecific, name = "extraCurricularProgram-specific"),
    path('extraCurricularProgram-create/', views.extraCurricularProgram_post,name ="extraCurricularProgram-create"),
    path('extraCurricularProgram-update/<str:pk>', views.extraCurricularProgram_put,name ="extraCurricularProgram-update"),
    path('extraCurricularProgram-delete/<str:pk>', views.extraCurricularProgram_delete,name ="extraCurricularProgram-delete"),
    
    path('award/', views.award_get, name = "award"),
    path('award/<str:pk>', views.award_getspecific, name = "award-specific"),
    path('award-create/', views.award_post,name ="award-create"),
    path('award-update/<str:pk>', views.award_put,name ="award-update"),
    path('award-delete/<str:pk>', views.award_delete,name ="award-delete"),
    
    path('extracurricularOfferings/', views.extracurricularOfferings_get, name = "extracurricularOfferings"),
    path('extracurricularOfferings/<str:pk>', views.extracurricularOfferings_getspecific, name = "extracurricularOfferings-specific"),
    path('extracurricularOfferings-create/', views.extracurricularOfferings_post,name ="extracurricularOfferings-create"),
    path('extracurricularOfferings-update/<str:pk>', views.extracurricularOfferings_put,name ="extracurricularOfferings-update"),
    path('extracurricularOfferings-delete/<str:pk>', views.extracurricularOfferings_delete,name ="extracurricularOfferings-delete"),
    
    path('staff/', views.staff_get, name = "staff"),
    path('staff/<str:pk>', views.staff_getspecific, name = "staff-specific"),
    path('staff-create/', views.staff_post,name ="staff-create"),
    path('staff-update/<str:pk>', views.staff_put,name ="staff-update"),
    path('staff-delete/<str:pk>', views.staff_delete,name ="staff-delete"),
    
    path('fieldOfStudy/', views.fieldOfStudy_get, name = "fieldOfStudy"),
    path('fieldOfStudy/<str:pk>', views.fieldOfStudy_getspecific, name = "fieldOfStudy-specific"),
    path('fieldOfStudy-create/', views.fieldOfStudy_post,name ="fieldOfStudy-create"),
    path('fieldOfStudy-update/<str:pk>', views.fieldOfStudy_put,name ="fieldOfStudy-update"),
    path('fieldOfStudy-delete/<str:pk>', views.fieldOfStudy_delete,name ="fieldOfStudy-delete"),
    
    path('course/', views.course_get, name = "course"),
    path('course/<str:pk>', views.course_getspecific, name = "course-specific"),
    path('course-create/', views.course_post,name ="course-create"),
    path('course-update/<str:pk>', views.course_put,name ="course-update"),
    path('course-delete/<str:pk>', views.course_delete,name ="course-delete"),
    
    path('courseTeaching/', views.courseTeaching_get, name = "courseTeaching"),
    path('courseTeaching/<str:pk>', views.courseTeaching_getspecific, name = "courseTeaching-specific"),
    path('courseTeaching-create/', views.courseTeaching_post,name ="courseTeaching-create"),
    path('courseTeaching-update/<str:pk>', views.courseTeaching_put,name ="courseTeaching-update"),
    path('courseTeaching-delete/<str:pk>', views.courseTeaching_delete,name ="courseTeaching-delete"),
    
    path('alumniHas/', views.alumniHas_get, name = "alumniHas"),
    path('alumniHas/<str:pk>', views.alumniHas_getspecific, name = "alumniHas-specific"),
    path('alumniHas-create/', views.alumniHas_post,name ="alumniHas-create"),
    path('alumniHas-update/<str:pk>', views.alumniHas_put,name ="alumniHas-update"),
    path('alumniHas-delete/<str:pk>', views.alumniHas_delete,name ="alumniHas-delete"),
    
    path('ranking/', views.ranking_get, name = "ranking"),
    path('ranking/<str:pk>', views.ranking_getspecific, name = "ranking-specific"),
    path('ranking-create/', views.ranking_post,name ="ranking-create"),
    path('ranking-update/<str:pk>', views.ranking_put,name ="ranking-update"),
    path('ranking-delete/<str:pk>', views.ranking_delete,name ="ranking-delete"),
    
    path('gruUser/', views.gruUser_get, name = "gruUser"),
    path('gruUser/<str:pk>', views.gruUser_getspecific, name = "gruUser-specific"),
    path('gruUser-create/', views.gruUser_post,name ="gruUser-create"),
    path('gruUser-update/<str:pk>', views.gruUser_put,name ="gruUser-update"),
    path('gruUser-delete/<str:pk>', views.gruUser_delete,name ="gruUser-delete"),
    
    path('preference/', views.preference_get, name = "preference"),
    path('preference/<str:pk>', views.preference_getspecific, name = "preference-specific"),
    path('preference-create/', views.preference_post,name ="preference-create"),
    path('preference-update/<str:pk>', views.preference_put,name ="preference-update"),
    path('preference-delete/<str:pk>', views.preference_delete,name ="preference-delete"),
    
    path('preferredUni/', views.preferredUni_get, name = "preferredUni"),
    path('preferredUni/<str:pk>', views.preferredUni_getspecific, name = "preferredUni-specific"),
    path('preferredUni-create/', views.preferredUni_post,name ="preferredUni-create"),
    path('preferredUni-update/<str:pk>', views.preferredUni_put,name ="preferredUni-update"),
    path('preferredUni-delete/<str:pk>', views.preferredUni_delete,name ="preferredUni-delete"),
    
    path('preferenceContain/', views.preferenceContain_get, name = "preferenceContain"),
    path('preferenceContain/<str:pk>', views.preferenceContain_getspecific, name = "preferenceContain-specific"),
    path('preferenceContain-create/', views.preferenceContain_post,name ="preferenceContain-create"),
    path('preferenceContain-update/<str:pk>', views.preferenceContain_put,name ="preferenceContain-update"),
    path('preferenceContain-delete/<str:pk>', views.preferenceContain_delete,name ="preferenceContain-delete"),
    
    path('sport/', views.sport_get, name = "sport"),
    path('sport/<str:pk>', views.sport_getspecific, name = "sport-specific"),
    path('sport-create/', views.sport_post,name ="sport-create"),
    path('sport-update/<str:pk>', views.sport_put,name ="sport-update"),
    path('sport-delete/<str:pk>', views.sport_delete,name ="sport-delete"),
    
    path('club/', views.club_get, name = "club"),
    path('club/<str:pk>', views.club_getspecific, name = "club-specific"),
    path('club-create/', views.club_post,name ="club-create"),
    path('club-update/<str:pk>', views.club_put,name ="club-update"),
    path('club-delete/<str:pk>', views.club_delete,name ="club-delete"),
    

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