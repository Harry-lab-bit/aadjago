from django.urls import path
from protfolio import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('internshipdetails', views.internshipdetails, name="internshipdetails"),
]
