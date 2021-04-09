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
    path('alumni/', views.alumniget, name = "alumni"),
    path('alumni-create/', views.alumnipost,name ="alumni-create"),
    path('alumni-update/<str:pk>', views.alumniput,name ="alumni-update"),
    path('alumni-delete/<str:pk>', views.alumnidelete,name ="alumni-delete"),
    url(r'^professor/', views.ProfessorList.as_view()),
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