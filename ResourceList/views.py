from django.shortcuts import render
from .models import Course, Project, WebSites, FrameWorks, WebDevelopment, Languages, YoutubeVideos


# Create your views here.

def index(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
    }
    return render(request, 'index.html', details)


def course(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
        "details": Course.objects.all().order_by('name'),
    }
    return render(request, 'display.html', details)


def project(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
        "details": Project.objects.all().order_by('name'),
    }
    return render(request, 'display.html', details)


def website(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
        "details": WebSites.objects.all().order_by('name'),
    }
    return render(request, 'display.html', details)


def language(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
        "details": Languages.objects.all().order_by('name'),
    }
    return render(request, 'display.html', details)


def framework(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
        "details": FrameWorks.objects.all().order_by('name'),
    }
    return render(request, 'display.html', details)


def webdevelopment(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
        "details": WebDevelopment.objects.all().order_by('name'),
    }
    return render(request, 'display.html', details)


def youtubevideos(request):
    details = {
        "cour": Course.objects.all().order_by('name'),
        "proj": Project.objects.all().order_by('name'),
        "lang": Languages.objects.all().order_by('name'),
        "frame": FrameWorks.objects.all().order_by('name'),
        "youchan": YoutubeVideos.objects.all().order_by('name'),
        "webdev": WebDevelopment.objects.all().order_by('name'),
        "impweb": WebSites.objects.all().order_by('name'),
        "details": YoutubeVideos.objects.all().order_by('name'),
    }
    return render(request, 'display.html', details)
