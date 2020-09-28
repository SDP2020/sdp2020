from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Post
from .w3_web_scraping import scrap_w3
from .wits_web_scraping import init_web_scrap

# Create your views here.
 # The student number of the user

def home(request):
    return render(request,'blog/home.html') #these files are out of the directories of the prohects


def about(request):
    context={
        'posts': Post.objects.all()
    }
    username, password = request.GET.get('username', None), request.GET.get('password', None) # Get the username and password of the student
    # if the user the about page has been rendered
    if type(username) == str: 
        results = init_web_scrap(username, password)
        username, password = None, None
        return JsonResponse(results)

    return render(request,'blog/about.html', context)#these files are out of the directories of the prohects


def web_scraping(request):
    search = request.GET.get("search_query", None)
    if type(search) == str:
        print(search)
        scrap_results = scrap_w3(search)
        return JsonResponse({"Name": scrap_results})
    return render(request, 'blog/web_scraping.html')

