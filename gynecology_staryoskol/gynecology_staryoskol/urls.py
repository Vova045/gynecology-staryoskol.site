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
from .decorators import check_recaptcha

urlpatterns = [
    path('', check_recaptcha(views.home), name='home'),
    path('diagnostics', check_recaptcha(views.diagnostics), name='diagnostics'),
    path('for_clients', check_recaptcha(views.for_clients), name='for_clients'),
    path('department', check_recaptcha(views.department), name='department'),
    path('hospital', check_recaptcha(views.hospital), name='hospital'),
    path('contacts', check_recaptcha(views.contacts), name='contacts'),
    path('services', check_recaptcha(views.services), name='services'),
    path('doctors', check_recaptcha(views.doctors), name='doctors'),
    path('questions_and_answers', check_recaptcha(views.questions_and_answers), name='questions_and_answers'),
    path('privacy_policy', check_recaptcha(views.privacy_policy), name='privacy_policy'),
    path('paid_services', check_recaptcha(views.paid_services), name='paid_services'),
    path('consultations', check_recaptcha(views.consultations), name='consultations'),
    path('surgery', check_recaptcha(views.surgery), name='surgery'),
    path('client_support', check_recaptcha(views.client_support), name='client_support'),
    path('hospital_support', check_recaptcha(views.hospital_support), name='hospital_support'),
    path('emergency_care', check_recaptcha(views.emergency_care), name='emergency_care'),
    path('non-resident_clients', check_recaptcha(views.non_resident_clients), name='non-resident_clients'),
]


