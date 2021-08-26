from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        PUBLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
        UNLISTED = 'UN', 'Unlisted'
        PRIVATE = 'PR','Private'

    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=220)
    active = models.BooleanField(default=True)

    # timestamp
    # updated
    state = models.CharField(max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)
    publish_timestamps = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    @property
    def is_published(self):
        return self.active

    def save(self, *args, **kwargs):
        if self.state == self.VideoStateOptions.PUBLISH and self.publish_timestamps is None:
            self.publish_timestamps = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.publish_timestamps = None

        super().save(*args, **kwargs)


class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'
