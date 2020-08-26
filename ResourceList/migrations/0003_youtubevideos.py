# Generated by Django 3.0.7 on 2020-08-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceList', '0002_auto_20200824_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('url', models.CharField(max_length=50)),
                ('images', models.FileField(upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Youtube Videos',
            },
        ),
    ]
