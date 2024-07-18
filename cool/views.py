from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Django Task-2</h1>")

def swag(request):
    return render(request, "main/index.html")

def swagme(request):
    return render(request, "main/swagme.html")

def swagmeandyou(request):
    return render(request, "main/swagmeandyou.html")