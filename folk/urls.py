from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('',views.home, name="home"),
    path('about/',views.about,name="about"),
    path('upload/',views.upload,name="upload"),
    path('login/', auth_views.LoginView.as_view(template_name='folk/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('story/<int:story_id>/',views.view_story,name='view_story'),
    path('story/<int:id>/delete/', views.delete_story, name='delete_story'),
    path('story/all/',views.story_list,name='story_list'),
]