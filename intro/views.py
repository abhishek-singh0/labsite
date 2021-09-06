from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'intro/dashboard.html')

def index(request):
    return render(request, 'intro/index.html')

def signUp(request):
    return render(request, 'intro/signUp.html')

def login(request):
    return render(request, 'intro/login.html')


def aboutlab(request):
    return render(request, 'intro/about_lab.html')