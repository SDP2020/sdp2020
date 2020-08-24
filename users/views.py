from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student
from .models import Course

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('blog-about')
    else:    
        form =UserCreationForm()
    return render(request,'users/register.html',{'forms':form})

def mycourses(request):
    context={
        'posts': Student.objects.get(student_number="2020811").courses.all()
    }
    return render(request,'users/mycourses.html', context)