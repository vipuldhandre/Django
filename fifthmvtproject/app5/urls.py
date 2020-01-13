from django.urls import path
from app5.views import tester,developer,combine

urlpatterns = [
    path('tester/',tester),
    path('developer/',developer),
    path('combine/',combine),
]
