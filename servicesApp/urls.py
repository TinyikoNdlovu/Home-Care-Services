from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #GET REQUEST
    path('about/', views.about_us, name="about_us"),
    path('services/', views.services, name="services")
]

