from django.urls import path
from app.views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as v

urlpatterns = [

    path('function/',index),
    path('class/',HomeView.as_view()),
    path('generic/',TemplateView.as_view(template_name='app/generic.html')),
    path('login/',v.LoginView.as_view(template_name='app/login.html')),
    path('logout/',v.LogoutView.as_view(template_name='app/login.html')),

]
