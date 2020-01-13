from django.shortcuts import render

def login(request):
    return render(request,"testapp/index.html")

# Create your views here.
def about(request):
    return render(request,"testapp/about.html")
