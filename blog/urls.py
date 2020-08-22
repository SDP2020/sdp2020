from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.home, name='blog-home'),
    url(r'^about/', views.about, name='blog-about'),
     url(r'^mycourses/', views.mycourses, name='mycourses')
]