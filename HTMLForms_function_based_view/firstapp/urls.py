from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('addemployee/',add_employee),
    path('delete/<int:eid>/',del_employee),
    path('update/<int:eid>/',update_employee),
    path('updateemployee/',update_database),
]
