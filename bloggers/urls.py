from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('blogs', views.bloggerhome, name='bloggerhome'),
    path('<str:slug>', views.blogpost, name='blogpost'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)