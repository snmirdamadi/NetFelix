# Generated by Django 3.2.6 on 2021-08-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_video_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publish_timestampe',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
