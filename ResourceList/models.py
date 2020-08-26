from django.db import models


# Create your models here.

class WebSites(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    url = models.CharField(max_length=50)
    images = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Websites'


class Course(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    url = models.CharField(max_length=50)
    images = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Courses'


class Project(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    url = models.CharField(max_length=50)
    images = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Projects'


class Languages(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    url = models.CharField(max_length=50)
    images = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'


class FrameWorks(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    url = models.CharField(max_length=50)
    images = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Framesworks'


class WebDevelopment(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    url = models.CharField(max_length=50)
    images = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Web Development'


class YoutubeVideos(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    url = models.CharField(max_length=50)
    images = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Youtube Videos'
