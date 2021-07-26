from django.shortcuts import render, HttpResponse

# Create your views here.

def bloggerhome(request):
    return render(request, 'bloggers/home_bloggers.html')

def blogpost(request, slug):
    return render(request, 'bloggers/blog_post.html')