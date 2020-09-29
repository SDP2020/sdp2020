from django.test import TestCase
from .models import Post
import unittest
from django.test import Client
from .urls import urlpatterns
from django.urls import reverse
import pytest

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(course_code="TESTCOR",course_name="Computer Sciences")
    
    def testPost1Exists(self):
        course_code= Post.objects.get(course_code="TESTCOR")
        self.assertEqual(course_code.course_name,"Computer Sciences")
    
    def testPost2Exists(self):
        course_name= Post.objects.get(course_name="Computer Sciences")
        self.assertEqual(course_name.course_name,"Computer Sciences")

class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/web_scraping/')
        self.assertEqual(response.status_code, 404)

    def test_index(self):
        client = Client()
        response = client.get('/google_scholar/ajax/?search_query=complex%20equations/')
        self.assertEqual(response.status_code, 404)


class GoogleScholar(TestCase):

    def test_correct_results(self):
        response = self.client.post('/google_scholar/')
        self.assertEqual(response.status_code, 200)

        self.assertJSONEqual(force_text(response.content), {'status': 'success'})

class test_web_scraing(TestCase):

    def test_correct_results(self):
        response = self.client.post('/web_scrap/')
        self.assertEqual(response.status_code, 200)

        self.assertJSONEqual(force_text(response.content), {'status': 'success'})