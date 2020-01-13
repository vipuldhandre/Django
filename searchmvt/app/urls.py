from django.urls import path
from app.views import index,search

urlpatterns = [
    path('index/',index),
    path('search/',search),
]
