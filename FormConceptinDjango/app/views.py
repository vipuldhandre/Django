from django.shortcuts import render,HttpResponseRedirect
from app.models import Book
from app.forms import BookForm,UserCreationForm


def book(request):
    if request.method=="POST":
        print(request.POST)
        name=request.POST.get('key1')
        author=request.POST.get('key2')
        price=request.POST.get('key3')
        #print(request.POST)
        Book.objects.create(bname=name,bauthor=author,bprice=price)
        return HttpResponseRedirect('/index/')

    else:
        return render(request,'app/index.html')

def form(request):
    form=BookForm(request.POST)
    if request.method=="POST":

        if form.is_valid():
            print(request.POST)
            Book.objects.create(bname=request.POST.get('bname'),bauthor=request.POST.get('bauthor'),bprice=request.POST.get('bprice'))
            return HttpResponseRedirect('/forms/')
    #form=BookForm()
    if form.errors:
        formerror=form.errors
    book = Book.objects.all()
    return render(request,'app/forms.html',{'form':form,'book':book,'formerror':formerror})

def modelform(request):
    form=UserCreationForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/modelform/")
    return render(request,'app/modelform.html',{'form':form})








# Create your views here.
