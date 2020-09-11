from django.shortcuts import render
from .models import Post
from .web_scraping import scrap_w3
from django.http import JsonResponse, HttpResponse
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
    student_number = request.GET.get('student_number', None) # The student number of the user 
    return JsonResponse({"student_number": str(student_number), "courses": "COMS3008,COMS3005,COMS3001"})



def web_scraping(request):
    search = request.GET.get("search_query", None)
    if type(search) == str:
        print(search)
        scrap_results = scrap_w3(search)
        return JsonResponse({"Name": "Tyler", "Surname": "May"})
    return render(request, 'blog/web_scraping.html')


def web_scrap(request):
    # TODO Implement web scraping here
    pass


