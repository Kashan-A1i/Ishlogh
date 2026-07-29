from django.shortcuts import render
from .models import Story

# Create your views here.

def about(request):
    return render(request, "folk/about.html")

def upload(request):
    return render(request,"folk/upload.html")

def login(request):
    pass

def home(request):
    stories = Story.objects.all()
    context = {
        'stories' : stories
    }
    return render(request, 'folk/home.html',context)

