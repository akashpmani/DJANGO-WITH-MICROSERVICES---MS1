from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    users = User.objects.all()
    return render(request, 'test.html',{'users':users})

def home1(request):
    return HttpResponse("Hello World!")