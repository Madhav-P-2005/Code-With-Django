# from django.shortcuts import render

# Create your views here.

# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello , world')