"""gynecology_staryoskol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from gynecology_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diagnostics', views.diagnostics, name='diagnostics'),
    path('for_clients', views.for_clients, name='for_clients'),
    path('department', views.department, name='department'),
    path('hospital', views.hospital, name='hospital'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),
    path('doctors', views.doctors, name='doctors'),
    path('questions_and_answers', views.questions_and_answers, name='questions_and_answers'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('paid_services', views.paid_services, name='paid_services'),
]


