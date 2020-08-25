from django.test import TestCase
from .models import Post
class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(course_code="TESTCOR",course_name="Computer Sciences")
    
    def testPost1Exists(self):
        course_code= Post.objects.get(course_code="TESTCOR")
        self.assertEqual(course_code.course_name,"Computer Sciences")
    
    def testPost2Exists(self):
        course_name= Post.objects.get(course_name="Computer Sciences")
        self.assertEqual(course_name.course_name,"Computer Sciences")