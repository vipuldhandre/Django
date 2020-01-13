from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
# Create your views here.

'''function based view'''
def index(request):
    return render(request,'templateapp/index.html')


'''Class Based View '''
class HomeView(View):
    template_name='templateapp/home.html'
    def get(self,request):
        return render(request,self.template_name)

'''Template Based View
class HomeTemplate(TemplateView):
    template_name='templateapp/template.html'
'''
