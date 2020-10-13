from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)

#     def __str__(self):
#         return '%s, %s' %(self.name, self.student_number)
    
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.student.save() # if you run into problem's try changing profile to student

class Student(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    courses = models.TextField(max_length=500000, blank=True)
    student_number = models.IntegerField(max_length=8, primary_key=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.sjtudent.save()
