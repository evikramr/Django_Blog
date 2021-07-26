from django.shortcuts import render, redirect
from . models import User
from . forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from . forms import *
# Create your views here.

def home(request):
    User.objects.all()
    return render(request, 'blog/home_blog.html')

def about(request):    
    return render(request, 'blog/about.html')

def contact(request):    
    return render(request, 'blog/contact.html')

def Reader_Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form_r = form.save(commit=False)
            form_r.is_reader = True
            form_r.set_password(form_r.password)
            form.save()

        else:
            print(form.errors)
            return HttpResponse('form not valid')

    else:
        form = UserRegisterForm()
    return render(request, 'blog/reader_form.html', {'form':form})


def Blogger_Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form_r = form.save(commit=False)
            form_r.is_blogger = True
            form_r.set_password(form_r.password)
            form.save()
 
        else:
            print(form.errors)
            return HttpResponse('form not valid')

    else:
        form = UserRegisterForm()
    return render(request, 'blog/reader_form.html', {'form':form})

def User_Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and is_reader:
                login(request, user)
                return redirect('Reader_Register')

            elif user.is_active and is_blogger:
                login(request, user)
                return redirect('Blogger_Register')
            else:
                return HttpResponse('User is Not Active')
        else:
            return HttpResponse('username or password is wrong')
    else:
        return render(request, 'accounts/login_form.html', {})

 

