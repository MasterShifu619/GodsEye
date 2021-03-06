# Generated by Django 3.0.5 on 2020-05-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_video_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_info',
            name='any_violence',
            field=models.CharField(default='No', max_length=10),
        ),
        migrations.AddField(
            model_name='video_info',
            name='ifps',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='video_info',
            name='no_of_people',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='video_info',
            name='ofps',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='video_info',
            name='time_taken',
            field=models.IntegerField(default=10),
        ),
    ]
