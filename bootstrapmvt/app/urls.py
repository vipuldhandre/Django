from django.urls import path
from app.views import index,tech,sports,politics
urlpatterns = [

    path('index/',index),
    path('technews/',tech),
    path('sportnews/',sports),
    path('politicsnews/',politics),

]
