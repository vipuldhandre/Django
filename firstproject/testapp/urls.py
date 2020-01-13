from django.urls import path
from testapp.views import date,list,dict

urlpatterns = [

    path('date/',date),
    path('list/',list),
    path('dict/',dict),

]
