from testapp.views import login,about
from django.urls import path

urlpatterns = [
    path('login/',login),
    path('about/',about),
    ]
