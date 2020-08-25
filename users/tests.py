from django.test import TestCase
from .models import Student, Course

class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="TestCourse", course_code="TEST0000")
    
    def testCourseExists(self):
        print("hello", Course.objects.all())
        self.assertEqual(Course.objects.get(name="TestCourse", course_code="TEST0000").get_course_name(), "TestCourse")
    

