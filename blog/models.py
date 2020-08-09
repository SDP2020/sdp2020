from django.db import models

class Post(models.Model):
    course_code = models.CharField(max_length=8)
    course_name = models.TextField()
# Create your models here.
