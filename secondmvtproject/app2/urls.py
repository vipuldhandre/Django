from django.urls import path
from app2.views import book,mobile,combine

urlpatterns = [
    path('bookdata/',book),
    path('mobiledata/',mobile),
    path('combine/',combine),
]
