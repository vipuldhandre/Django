from django.urls import path
from app3.views import set,alex,addition

urlpatterns = [

    path('set/',set),
    path('alex/',alex),
    path('addition/',addition),

]
