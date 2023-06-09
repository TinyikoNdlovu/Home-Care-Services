from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about_us(request):
    return render(request, 'about.html', {})

def services(request):
    categories = [
    {
        'name': 'Plumber',
        'service_Main_Img ': 'Service 1',
        'description': 'Specializes ininstalling and maintaining systems',
        'provider': 'William',
    },
    {
        'name': 'Carpentry',
        'service_Main_Img': 'Service 2',
        'description': 'Cutting,shaping and installing of building materials',
        'provider': 'Martin',
    }
]
    return render(request, 'services.html', {"services": categories})

