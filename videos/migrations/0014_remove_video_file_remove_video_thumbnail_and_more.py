# Generated by Django 4.0.3 on 2022-04-09 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_alter_video_author_alter_video_filename_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
        migrations.RemoveField(
            model_name='video',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnailName',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]