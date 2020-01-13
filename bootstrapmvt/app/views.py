from django.shortcuts import render
from app.models import Tech,Sports,Politics

def index(request):
    msg="Hi Handsome!"
    return render(request,'app/index.html',context={'msg':msg})

def tech(request):
    data={'1':'Electron moves around nucleus.','2':'Mass of Human on earth is multiplied by gravity of earth.'}
    data1=Tech.objects.all()
    return render(request,'app/technews.html',context={'data':data,'data1':data1})

def sports(request):
    data={'1':'India beats West Indies in Test Series by 2-0.','2':'India retains first position after West Indies Tour in Test.'}
    data1=Sports.objects.all()
    return render(request,'app/sportnews.html',context={'data':data,'data1':data1})

def politics(request):
    data={'1':'Sharad Pawar decided to switch from NCP to BJP.','2':'Pakistan PM going to take Indian Nationality.'}
    data1=Politics.objects.all()
    return render(request,'app/politicsnews.html',context={'data':data,'data1':data1})


# Create your views here.
