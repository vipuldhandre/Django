from django.urls import path
from app.views import HomeView
urlpatterns = [

    path('home/',HomeView.as_view()),

]
