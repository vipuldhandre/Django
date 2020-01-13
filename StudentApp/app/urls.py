from django.urls import path
from app.views import index,addstudent,deletestudent,studentform


urlpatterns = [

    path('index/',index),
    path('home/',addstudent),
    path('delete/<int:id>/',deletestudent),
    path('studentform/',studentform),

]
