# Generated by Django 4.0.3 on 2022-04-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_alter_video_file_alter_video_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='fileName',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
