from django.urls import path
from .views import *


urlpatterns = [
    path('home/',home),
    path('add/',add),
    path('delete/<int:eid>/',delete),
    path('update/<int:eid>/',update),
]
