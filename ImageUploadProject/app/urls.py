from django.urls import path
from app.views import *
from django.contrib.auth import views
urlpatterns = [
    path('index/',index),
    path('login/',views.LoginView.as_view(template_name='app/login.html')),
    path('logout/',views.LogoutView.as_view(template_name='app/login.html')),
    #path('class/',HomeView.as_view()),
]
