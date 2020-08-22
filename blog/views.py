from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse #HttpResponse libraries

# Create your views here.
 # The student number of the user

def home(request):
    return render(request,'blog/home.html') #these files are out of the directories of the prohects

def about(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request,'blog/about.html', context)#these files are out of the directories of the prohects

def mycourses(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/mycourses.html', context)