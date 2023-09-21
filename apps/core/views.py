from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'core/index.html')


def login(request: HttpRequest):
    return render(request, 'core/pages/login.html')