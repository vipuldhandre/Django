from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required


""" Function based view """
@login_required
def index(request):

    return render(request,'app/function.html')

""" Class based view """
class HomeView(View):
    template_name="app/class.html"
    def get(self,request):
        return render(request,self.template_name)

"""Generic class based view
class HomeTemplate(TemplateView):
    template_name='app/generic.html'
"""

# Create your views here.
