from django.urls import path
from demoapp import views
urlpatterns = [
    path('home/',views.home),
    path('cdt/',views.cdatetime),
    path('gm/',views.goodmorning),
    path('ga/',views.goodafternoon),
    path('ge/',views.goodevening),
    path('gn/',views.goodnight)
]
