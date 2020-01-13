from django.urls import path
from orderapp.views import OrderView,OrderDetailsView


urlpatterns = [

    path('order/',OrderView.as_view()),
    path('orderdetails/',OrderDetailsView.as_view()),
]
