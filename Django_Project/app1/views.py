from django.shortcuts import render
from django.http import HttpResponse

def anyview(request):
    return HttpResponse("<h1>Any View</h1>")

# Create your views here.
