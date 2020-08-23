from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
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


def enrolledCourse(request):
    return render(request, 'blog/enrolledCourse.html', {"tiltle":"Enrolled Courses"})


def ajax_get_courses(request):
    print("Hello world")
    student_number = request.GET.get('student_number', None) # The student number of the user
    '''
        Get user courses based on student number
    '''
    print("\n"*2)
    print(student_number)
    print("\n"*2)
    return JsonResponse({student_number: str(student_number), courses: "COMS3008,COMS3005,COMS3001"})