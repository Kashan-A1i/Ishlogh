from django.shortcuts import render,redirect
from .models import Story
from django.contrib.auth import login
from .forms import CustomSignupForm
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

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomSignupForm()
        
    return render(request, 'folk/signup.html', {'form': form})

