from django.shortcuts import render
from .models import Lecturer,Professor

def lecturer(request):
    msg="Lecturer info:"
    lecturerdata=Lecturer.objects.all()
    return render(request,'app/lecturerdata.html',context={'msg':msg,'lecturerdata':lecturerdata})


def professor(request):
    msg="Professor Info:"
    professordata=Professor.objects.all()
    return render(request,'app/professordata.html',context={'msg':msg,'professordata':professordata})

def combine(request):
    msg1="Lecturer Info:"
    msg2="Professor Info:"
    lecturerdata=Lecturer.objects.all()
    professordata=Professor.objects.all()
    return render(request,'app/combine.html',context={'msg1':msg1,'msg2':msg2,'lecturerdata':lecturerdata,'professordata':professordata})

# Create your views here.
