from django.urls import path
from customerapp.views import StateView,DistrictView,CityView,CustomerDetailsView


urlpatterns = [

    path('state/',StateView.as_view()),
    path('district/',DistrictView.as_view()),
    path('city/',CityView.as_view()),
    path('customerdetails/',CustomerDetailsView.as_view()),


]
