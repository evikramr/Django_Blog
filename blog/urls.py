from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('Reader_Register', views.Reader_Register, name='Reader_Register'),
    path('Blogger_Register', views.Blogger_Register, name='Blogger_Register'),
    path('User_Login', views.User_Login, name='User_Login'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)