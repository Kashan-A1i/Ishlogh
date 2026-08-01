from django.shortcuts import render, redirect
from .models import Story,UserProfile
from django.contrib.auth import login as auth_login
from .forms import CustomSignupForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,StoryForm

# Create your views here.

def about(request):
    return render(request, "folk/about.html")

@login_required
def upload(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES) 
        
        if form.is_valid():
            new_story = form.save(commit=False) 
            new_story.uploader = request.user 
            new_story.save() 
            return redirect('home') 
    else:
        form = StoryForm()
    return render(request, 'folk/upload.html', {'form': form})

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
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    unique_regions_count = Story.objects.filter(uploader=user).values('region').distinct().count()
    recent_stories = Story.objects.filter(uploader=user)[:3]
    return render(request, 'folk/profile.html', {
        'user': user,
        'user_profile':user_profile,
        'unique_regions': unique_regions_count,
        'recent_stories': recent_stories,
    })
@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user_profile)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
            
    else:
        form = ProfileUpdateForm(instance=user_profile)

    return render(request, 'folk/edit_profile.html', {'form': form})

