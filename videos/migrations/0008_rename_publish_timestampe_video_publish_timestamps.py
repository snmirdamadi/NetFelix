# Generated by Django 3.2.6 on 2021-08-26 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_video_publish_timestampe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='publish_timestampe',
            new_name='publish_timestamps',
        ),
    ]
