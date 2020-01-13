from django.urls import path
from app.views import index,addtodo,deletetodo

urlpatterns = [

        path('index/',index),
        path('home/',addtodo),
        path('delete/<int:todo_id>/',deletetodo),

]
