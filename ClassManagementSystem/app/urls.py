from django.urls import path
from app.views import index,search
from django.contrib.auth import views as v

urlpatterns = [

    path('index/',index),
    path('search/',search),
    path('login/',v.LoginView.as_view(template_name='app/login.html')),
    path('logout/',v.LogoutView.as_view(template_name='app/login.html')),
]
