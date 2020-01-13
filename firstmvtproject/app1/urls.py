from django.urls import path
from app1.views import Studata,Empdata,Combine

urlpatterns = [

    path('studata/',Studata),
    path('empdata/',Empdata),
    path('combine/',Combine),

]
