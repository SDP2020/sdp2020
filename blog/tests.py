from django.test import TestCase
from .import models
from django.urls import resolve, reverse
from django.test import TestCase
from blog.models import Post

class PostTest(TestCase):
    def create_post(self,course_code="COMS3000",course_name="Parallel Computing"):
        return Post.objects.create(course_code=course_code,course_name=course_name)

    def test_post_creation(self):
        p= self.create_post()
        self.assertTrue(isinstance,(p, Post))
        self.assertEqual(p.__unicode__(),p.course_code)



class TestPost(TestCase):
    def test_expensemodels(self):
        Post = models(
            course_code='12233334',
            course_name='erhsjsdhdfs'
        )
        self.assertTrue(models.is_valid())

    def test_expenseform_nodata(self):
        Post = models(data={})
        self.assertFalse(models.is_valid())
        self.assertEquals(len(models.errors),2)
       
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, views.home)

    def test_about_view_status_code(self):
        url = reverse('blog-about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_url_resolves_home_view(self):
        view = resolve('/about')
        self.assertEqual(view.func, views.about)


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_blog_home_(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    def test_index_blog_about_(self):
        url = reverse('blog-about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')