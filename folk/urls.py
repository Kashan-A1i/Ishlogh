from django.urls import path, include
from django.contrib import admin
from . import views
urlpatterns=[
    path('',views.home, name="home"),
    path('about/',views.about,name="about"),
    path('upload/',views.upload,name="upload"),
    path('login/',views.login,name="login")
]