from django.test import TestCase
from users.models import Course

class CourseTestCase(TestCase):
    def createCourse(self):
        Course.objects.create(name="test_course", course_code="TEST0000")
        Course.objects.create(name="test_course2", course_code="TEST0001")
        print(Course.objects)
        
    def testCourseExists(self):
        course1 = Course.objects.get(course_code="TEST0001")
        self.assertEqual(course1.get_course_name(), "test_course")