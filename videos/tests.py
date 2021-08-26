from django.test import TestCase

# Create your tests here.
from .models import Video


class VideoModelTestCase(TestCase):

    def setUp(self) -> None:
        Video.objects.create(title='This is my title')

    def test_valid_title(self):
        title = 'This is my title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

