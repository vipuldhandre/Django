from django.shortcuts import render,HttpResponseRedirect
from app.models import Student
from app.forms import StudentForm

def index(request):
    studata = Student.objects.all()
    return render(request,'app/index.html',context = {'studata':studata})

def addstudent(request):
    data = Student(sname = request.POST['key1'],srn = request.POST['key2'],sclass = request.POST['key3'],smarks = request.POST['key4'])
    data.save()
    print(request.POST)
    return HttpResponseRedirect('/index/')

def deletestudent(request,id):
    data = Student.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/index/')

def studentform(request):

    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():

            name=request.POST.get('key1')   #request.POST.get('key') is to fetch data from server.
            rn=request.POST.get('key2')
            cls=request.POST.get('key3')
            marks=request.POST.get('key4')
            Student.objects.create(sname=name,srn=rn,sclass=cls,smarks=marks)
            print(request.POST)
            return HttpResponseRedirect('/index/')
    else:
        form = StudentForm()
        return render(request,"app/formsvalid.html",{'form':form})
# Create your views here.
