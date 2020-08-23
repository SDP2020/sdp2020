from django.conf.urls import url
from django.urls import include, path
from . import views
from users import urls

urlpatterns = [
    url(r'^$', views.home, name='blog-home'),
    url(r'^about/', views.about, name='blog-about'),
    url(r'^enrolledcourses', views.enrolledCourse, name="enrolled_courses"), # display a page with the student's enrolled courses
    url(r'^enrolledcourses/ajax/getcourses/$', views.ajax_get_courses, name='ajax_get_courses'), # Get student courses
]