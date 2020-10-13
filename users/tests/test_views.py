from django.test import TestCase, Client
from users.models import Student, Course
import unittest

class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="TestCourse", course_code="TEST0000")

    def testCourseExists(self):
        print("hello", Course.objects.all())
        self.assertEqual(Course.objects.get(name="TestCourse", course_code="TEST0000").get_course_name(), "TestCourse")


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/mycourses/')
        self.assertEqual(response.status_code, 404)

    def test_index(self):
        client = Client()
        response = client.get('/customer/index/')
        self.assertEqual(response.status_code, 404)