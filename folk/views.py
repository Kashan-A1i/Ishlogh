from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "folk/home.html")
def about(request):
    return render(request, "folk/about.html")
def upload(request):
    return render(request,"folk/upload.html")
def login(request):
    pass