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
    path('', views.home, name='home'),
    path('training/', views.training, name='training'),
    path('contact/', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signupR', views.signupR, name='signupR'),
    path('studentrequest/', views.handelsignupstudent, name='student'),
    path('recruiterrequest/', views.handelsignuprecruiter, name='recruiter'),
    path('login/', views.handellogin, name='login'),
    path('emplogin/', views.handel_emp_login, name='emplogin'),
    path('logout/', views.handellogout, name='logout'),
    path('checkout/', views.checkout, name='Checkout'),
    path("handlerequest/", views.handlerequest, name='HandleRequest'),
    
    
    path('details/', views.studentdetail, name='details'),
    path('<int:post_id>/', views.apply_data, name='applydata'),

    

]
   
