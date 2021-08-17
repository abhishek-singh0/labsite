from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'intro/home.html')

def index(request):
    return render(request, 'intro/index.html')

