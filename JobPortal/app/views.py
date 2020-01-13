from django.shortcuts import render,HttpResponseRedirect
from app.models import Engineering,Management,Operations
from app.forms import EngineeringForm,ManagementForm,OperationsForm

def index(request):
    msg="Welcome to VIPUL's JOB PORTAL."
    return render(request,'app/index.html',context={'msg':msg})

def engineering(request):
    a="Python Developer at Amazon."
    b="Java Developer at Accenture."
    c=".Net Developer at Capgemini."
    dict={'1':a,'2':b,'3':c}
    data=Engineering.objects.all()
    return render(request,'app/engineering.html',context={'dict':dict,'data':data})

def management(request):
    a="Project Management Manager at Amazon."
    b="Release Management Associate at Accenture."
    c="Project Management Trainee at Capgemini."
    dict={'1':a,'2':b,'3':c}
    data=Management.objects.all()
    return render(request,'app/engineering.html',context={'dict':dict,'data':data})

def operations(request):
    a="Network security operations at Amazon."
    b="Maintainance & operations engineer at Accenture."
    c="Engineer IT operations at Capgemini."
    dict={'1':a,'2':b,'3':c}
    data=Operations.objects.all()
    return render(request,'app/engineering.html',context={'dict':dict,'data':data})

def e_form(request):

    if request.method=="POST":
        form=EngineeringForm(request.POST)
        if form.is_valid():
            name=request.POST.get('ejobs')
            Engineering.objects.create(ejobs=name)
            return HttpResponseRedirect("/eform/")

    else:
        form=EngineeringForm()
        return render(request,'app/eforms.html',context={'form':form})

def m_form(request):
    if request.method=="POST":
        form=ManagementForm(request.POST)
        if form.is_valid():
            name=request.POST.get('mjobs')
            Management.objects.create(mjobs=name)
            return HttpResponseRedirect("/mform/")

    else:
        form=ManagementForm()
        return render(request,'app/mforms.html',context={'form':form})

def o_form(request):
    if request.method=="POST":
        form=OperationsForm(request.POST)
        if form.is_valid():
            name=request.POST.get('ojobs')
            Management.objects.create(ojobs=name)
            return HttpResponseRedirect("/mform/")

    else:
        form=OperationsForm()
        return render(request,'app/oforms.html',context={'form':form})

# Create your views here.
