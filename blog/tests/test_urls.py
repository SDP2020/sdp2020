from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import home, about, query_google_scholar, web_scraping

class TestUrls(SimpleTestCase):

    def test_list_urls_home(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func, home)

    def test_list_urls_about(self):
        url = reverse('blog-about')
        self.assertEquals(resolve(url).func, about)

    def test_list_urls_webscrap(self):
        url = reverse('web_scraping')
        self.assertEquals(resolve(url).func, web_scraping)

    def test_list_urls_query(self):
        url = reverse('google_scholar')
        self.assertEquals(resolve(url).func, query_google_scholar)

    def test_list_urls_web_ajax(self):
        url = reverse('web_scrap')
        self.assertEquals(resolve(url).func, web_scraping)

    def test_list_urls_ajax_courses(self):
        url = reverse('courses')
        self.assertEquals(resolve(url).func, about)
