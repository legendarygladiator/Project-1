"""visudhajivam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .import views

from django.urls import include



urlpatterns = [
   
    path('', views.orgnize, name='orgnize'),
    path('fresherjobs/', views.fresherjob, name='fresher'),
    path('myjob/', views.myjob, name='myjob'),
    path('<int:post_id>/view_applies/', views.view_applies, name='view_applies'),
    path('<int:post_id>/job_details/', views.job_details, name='job_details')
]