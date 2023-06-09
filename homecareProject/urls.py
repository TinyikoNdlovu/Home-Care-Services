from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #servicesApp
    path('', include("servicesApp.urls"))
]
