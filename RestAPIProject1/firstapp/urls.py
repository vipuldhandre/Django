from django.urls import path
from .views import *

urlpatterns = [
    path('emp/',show_emp),
]
