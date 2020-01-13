from django.urls import path
from app4.views import submul,sub,mul

urlpatterns = [

    path('submul/',submul),
    path('sub/',sub),
    path('mul/',mul),

]
