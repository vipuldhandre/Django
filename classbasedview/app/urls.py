from django.urls import path
from app.views import home,Homeview

urlpatterns = [
    #path('index/',home),
    path('index/<int:var>/<var1>/',Homeview.as_view()),

]
