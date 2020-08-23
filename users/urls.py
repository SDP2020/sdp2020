from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^mycourses/', views.mycourses, name='mycourses'),
]