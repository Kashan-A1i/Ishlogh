from django.shortcuts import render, redirect
from .models import Story
from django.contrib.auth import login as auth_login
from .forms import CustomSignupForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
    return render(request, "folk/about.html")

@login_required
def upload(request):
    return render(request,"folk/upload.html")

def login(request):
    pass

def home(request):
    stories = Story.objects.all()
    context = {
        'stories' : stories
    }
    return render(request, 'folk/home.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomSignupForm()
        
    return render(request, 'folk/signup.html', {'form': form})
def profile(request):
    user=request.user
    return render(request, 'folk/profile.html', {
        'user': user
    })

