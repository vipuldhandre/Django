from django.urls import path
from app4.views import lecturer,professor,combine
urlpatterns = [
    path('lecturer/',lecturer),
    path('professor/',professor),
    path('combine/',combine),
]
