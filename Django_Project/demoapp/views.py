from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    return HttpResponse("<h2>This is Django App View</h2><br> <h3>My name is Vipul</h3> ")

def cdatetime(request):
    dt=datetime.datetime.now()
    return HttpResponse(f'<h1>The current date and time is:{dt}</h1>')

def goodmorning(request):
    return HttpResponse("<h3 style='color:red;'><center>Hello Vipul Good Morning!</center></h3><br>")

def goodafternoon(request):
    return HttpResponse("<h3 style='color:aqua;'><center>Hello Vipul Good Afternoon!</center></h3><br>")

def goodevening(request):
    return HttpResponse("<h3 style='color:orange;'><center>Hello Vipul Good Evening!</center></h3><br>")

def goodnight(request):
    return HttpResponse("<h3><center>Hello Vipul Good Night have sweet dreams!</h3>")
