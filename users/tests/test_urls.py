from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import mycourses

class TestUrls(SimpleTestCase):

    def test_urls_courses(self):
        url = reverse('mycourses')
        print(resolve(url))
        self.assertEquals(resolve(url).func, mycourses)