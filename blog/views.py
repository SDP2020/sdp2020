from django.shortcuts import render
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
def home(request):
    return render(request,'blog/home.html') #these files are out of the directories of the prohects

def about(request):
    return render(request,'blog/about.html',{'title':'About'})#these files are out of the directories of the prohects