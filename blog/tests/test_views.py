from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
from blog.views import query_google_scholar
import unittest
from blog.google_scholar import google_scholar
from blog.w3_web_scraping import scrap_w3
from re import search

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(course_code="TESTCOR", course_name="Computer Sciences")


    def testPost1Exists(self):
        course_code = Post.objects.get(course_code="TESTCOR")
        self.assertEqual(course_code.course_name, "Computer Sciences")


    def testPost2Exists(self):
        course_name = Post.objects.get(course_name="Computer Sciences")
        self.assertEqual(course_name.course_name, "Computer Sciences")


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/web_scraping/')
        self.assertEqual(response.status_code, 404)

    def test_index(self):
        client = Client()
        response = client.get('/google_scholar/ajax/?search_query=complex%20equations/')
        self.assertEqual(response.status_code, 404)

class test_google_scholar_results(TestCase):
    def test_comparing_results(self):
        res1="Design patterns for object-oriented software development"
        res2="FSoftware design patterns for information visualization"
        res3="Masonry arches: historical rules and modern mechanics"
        res =[
            res1,
            res2,
            res3]

        google=google_scholar("software design patterns")

        for res_ in res:
            if res_ not in google:
                return False
            else:
                return True

class test_web_scraping_results(TestCase):
    def test_web_scraping_results(self):
        res1="Java is a programming language."
        res2="python"
        res3="script"
        res =[
            res1,
            res2,
            res3]
        scrap_results = scrap_w3("java")
        for res_ in res:
            if res_ not in scrap_results:
                return False
            else:
                return True
