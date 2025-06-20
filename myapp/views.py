# Rendering Templates in Views 
from django.shortcuts import render

# Create your views here.

# myapp/views.py
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Hello , world')

# Django-Learning/myapp/views.py
def home(request):
    return render(request , 'home.html') 