# Generated by Django 4.0.3 on 2022-03-27 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_alter_video_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
