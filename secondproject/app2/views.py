from django.shortcuts import render

def tuple(request):
    msg="The Tuple is:"
    tup=((1,2,3,4),(5,6,7))
    return render(request,'app2/tuple.html',context={'msg':msg,'tup':tup})

def listintuple(request):
    msg="The list in tuple is:"
    list2tup=([1,2,3],[4,5,6])
    return render(request,'app2/listintup.html',context={'msg':msg,'list2tup':list2tup})

def dictintuple(request):
    msg="The Dictionary in Tuple is:"
    dict2tup=({1:'vipul',2:'vips'},{3:'Babu',4:'Vishal'})
    return render(request,'app2/dictintup.html',context={'msg':msg,'dict2tup':dict2tup})

# Create your views here.
