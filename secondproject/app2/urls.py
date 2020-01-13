from django.urls import path
from app2.views import tuple,listintuple,dictintuple

urlpatterns = [
    path('tuple/',tuple),
    path('listintuple/',listintuple),
    path('dictintuple/',dictintuple),

]
