from django.conf.urls import url
from django.urls import include, path
from . import views
from users import urls

urlpatterns = [
    url(r'^$', views.home, name='blog-home'),
    url(r'^about/', views.about, name='blog-about'),
    url(r'web_scraping/', views.web_scraping, name="web_scraping"),
    url(r'web_scraping/ajax/$', views.web_scraping, name="web_scrap"),
    url(r'ajax/courses/$', views.about, name="courses"),
]