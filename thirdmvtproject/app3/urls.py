from django.urls import path
from app3.views import born,human,combine

urlpatterns = [
    path('borndata/',born),
    path('humandata/',human),
    path('combine/',combine),
]
