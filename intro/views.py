from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'intro/dashboard.html')

def index(request):
    return render(request, 'intro/index.html')

