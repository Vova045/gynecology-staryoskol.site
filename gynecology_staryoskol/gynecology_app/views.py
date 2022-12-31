from django.shortcuts import render
from gynecology_staryoskol.settings import BASE_DIR

def home(request):
    print (BASE_DIR)
    return render (request, 'home.html',) 
