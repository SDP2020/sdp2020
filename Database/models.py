from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=256)
    course_code = models.CharField(max_length=10, primary_key=True);

    def __str__(self):
        return '%s %s' %(self.course_code, self.name)


    def get_course_name(self):
        '''
            Returns the name of the course
        '''
        return self.name

    
    def get_course_code(self):
        '''
            Returns the course code
        '''
        return self.course_code


    
class Student(models.Model):
    name = models.CharField(max_length=256)
    student_number = models.IntegerField(max_length=8, primary_key=True);
    courses = models.ManyToManyField(Course)
    password = models.CharField(max_length=256, default="password") # TODO this is just for testing purposes

    def __str__(self):
        return '%s, %s' %(self.name, self.student_number)
    

    def get_courses(self):
        '''
            return the courses that the user is registered for
        '''
        return self.courses