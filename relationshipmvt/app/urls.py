from django.urls import path
from app.views import company,programmer,languages,index

urlpatterns = [

    path('company/',company),
    path('programmer/',programmer),
    path('languages/',languages),
    path('index/',index),


]
