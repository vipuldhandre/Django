from django.urls import path
from app.views import book,form,modelform

urlpatterns = [

    path('index/',book),
    path('forms/',form),
    path('modelform/',modelform)

]
