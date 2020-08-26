from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('project/', views.project, name='project'),
    path('website/', views.website, name='website'),
    path('language/', views.language, name='language'),
    path('framework/', views.framework, name='framework'),
    path('webdevelopment/', views.webdevelopment, name='webdevelopment'),
    path('youtubevideos/', views.youtubevideos, name='youtubevideos'),
]
