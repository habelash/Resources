from django.contrib import admin
from .models import WebSites, Course, Project, Languages, FrameWorks, WebDevelopment, YoutubeVideos

admin.site.site_header = 'Resources'


# Register your models here.

class WebsiteNames(admin.ModelAdmin):
    list_display = ('name', 'url', 'discription')
    list_display_links = ['name', 'url']


admin.site.register(Course, WebsiteNames)
admin.site.register(Project, WebsiteNames)
admin.site.register(WebSites, WebsiteNames)
admin.site.register(Languages, WebsiteNames)
admin.site.register(FrameWorks, WebsiteNames)
admin.site.register(WebDevelopment, WebsiteNames)
admin.site.register(YoutubeVideos, WebsiteNames)


