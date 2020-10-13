import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from users.models import Student

from .models import Post
from .w3_web_scraping import scrap_w3
from .wits_web_scraping import init_web_scrap
from .google_scholar import google_scholar

# Create your views here.
 # The student number of the user

def home(request):
    return render(request,'blog/home.html') #these files are out of the directories of the prohects


def about(request):
    context={
        'posts': Post.objects.all()
    }
    username, password, state = request.user.username, request.GET.get('password', None), request.GET.get("state", None) # Get the username and password of the student
    print("\n\nThis is the username {username} and password {password}".format(username=username, password=password))
    # if the user the about page has been rendered
    
    if type(password) == str:
        try:
            user = Student.objects.filter(student_number=username)[0]
        
        except (IndexError):
            user = Student(student_number=username)

        results = init_web_scrap(username, password)
        user.courses = results
        user.save()

        password = None
        return JsonResponse(results)
   
    elif str(state) == "local":
        print("outside if condition")
        try:
            user = Student.objects.filter(student_number=username)[0]
            results = {}
            entry = user.courses.replace("{", "").replace("}","").replace("'","").split(",")
            # print(entry)
            for i in range(0, len(entry)):
                try:
                    index = entry[i].index(": course")
                    if i == 0:
                        key, value = entry[i][0: index], entry[i][index+2: ]
                    else:
                        key, value = entry[i][1: index], entry[i][index+2: ]
                except ValueError:
                    try:
                        index = entry[i].index(" resource")
                        if i == 0:
                            key, value = entry[i][0: index-1], entry[i][index+2: ]
                        else:
                            key, value = entry[i][1: index-1], entry[i][index+2: ]
                    except ValueError:
                        continue
                
                print("\n\n")
                print(key)
                print(value)
                results[key] = value
            print("\n\n after loop \n\n")
            return JsonResponse(results)
        except (IndexError):
            return JsonResponse({"User history not found, please click update resources to get your courses": "Error"})
    
    elif str(state) == "download":
        file_name = request.GET.get("file_name", None)
        # try:
        print("hgerjk")
        file_ = open(os.getcwd() + "/" + file_name + ".pdf", "rb").read()
        print(file_)
        #  sending response 
        response = HttpResponse(file_, content_type='pdf')
        response['Content-Disposition'] = 'attachment; filename={file_name}.pdf'.format(file_name=file_name)
        return response
        # except Exception:
            # handle file not exist case here
            # return JsonResponse({"File not found, please click update resources to get your courses": "Error"})

        return response

    return render(request,'blog/about.html', context)#these files are out of the directories of the prohects


def web_scraping(request):
    search = request.GET.get("search_query", None)
    if type(search) == str:
        print(search)
        scrap_results = scrap_w3(search)
        return JsonResponse({"Name": scrap_results})
    return render(request, 'blog/web_scraping.html')


def query_google_scholar(request):
    search = request.GET.get("search_query", None)
    if type(search) == str:
        print(search)
        scrap_results = google_scholar(search)
        return JsonResponse(scrap_results)
    return render(request, 'blog/google_scholar.html')
