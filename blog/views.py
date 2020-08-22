from django.shortcuts import render
from django.http import JsonResponse
#from django.http import HttpResponse #HttpResponse libraries

# Create your views here.
posts =[
    {
            'author': 'nasty C',
            'title' :   'hell naw',
            'content': 'never give up',
            'date-released' : '2017'
    },
    {
            'author': 'AKA',
            'title' :   'Run jozi',
            'content': 'the best',
            'date-released': '2013'
    }
]
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
    return JsonResponse({student_number: str(student_number), courses: "COMS3008,COMS3005,COMS3001"}) # Return a string containing all the courses they're enrolled in


def home(request):
    return render(request,'blog/home.html') #these files are out of the directories of the prohects


def about(request):
    return render(request,'blog/about.html',{'title':'About'})#these files are out of the directories of the prohects