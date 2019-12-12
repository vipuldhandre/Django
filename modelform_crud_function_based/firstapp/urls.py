from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',home),
    path('add/',add),
    path('delete/<int:id>/',delete),
    path('update/<int:id>/',update),
    path('login/',auth_views.LoginView.as_view(template_name='firstapp/login.html')),
    path('logout/',auth_views.LogoutView.as_view(template_name='firstapp/home.html')),

]
