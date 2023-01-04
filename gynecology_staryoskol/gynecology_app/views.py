from django.shortcuts import render


def home(request):
    return render (request, 'home.html',) 
def diagnostics(request):
    return render (request, 'diagnostics.html',) 
def for_clients(request):
    return render (request, 'for_clients.html',) 
def department(request):
    return render (request, 'department.html',) 
def hospital(request):
    return render (request, 'hospital.html',) 
def contacts(request):
    return render (request, 'contacts.html',) 
def services(request):
    return render (request, 'services.html',) 
def doctors(request):
    return render (request, 'doctors.html',) 
def questions_and_answers(request):
    return render (request, 'questions_and_answers.html',) 
def privacy_policy(request):
    return render (request, 'privacy_policy.html',) 
def paid_services(request):
    return render (request, 'paid_services.html',) 
