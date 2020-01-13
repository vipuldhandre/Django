from django.urls import path
from app.views import home,home2,home3,home4

urlpatterns = [

    path('home2/',home2),
    path('home3/',home3),
    path('home4/',home4),
    path('home/<slug:variable>/',home),
]
