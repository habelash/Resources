from django.shortcuts import render
from .models import Course, Project, WebSites, FrameWorks, WebDevelopment, Languages


# Create your views here.

def index(request):
    return render(request, 'index.html')


def course(request):
    details = Course.objects.all().order_by('name')
    return render(request, 'display.html', {'details': details})


def project(request):
    details = Project.objects.all().order_by('name')
    return render(request, 'display.html', {'details': details})


def website(request):
    details = WebSites.objects.all().order_by('name')
    return render(request, 'display.html', {'details': details})


def language(request):
    details = Languages.objects.all().order_by('name')
    return render(request, 'display.html', {'details': details})


def framework(request):
    details = FrameWorks.objects.all().order_by('name')
    return render(request, 'display.html', {'details': details})


def webdevelopment(request):
    details = WebDevelopment.objects.all().order_by('name')
    return render(request, 'display.html', {'details': details})


def youtubevideos(request):
    details = WebDevelopment.objects.all().order_by('name')
    return render(request, 'display.html', {'details': details})