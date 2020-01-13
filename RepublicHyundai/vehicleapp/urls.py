from django.urls import path
from vehicleapp.views import VehicleCategoryView,VehicleModelView,VehicleDetailsView

urlpatterns = [

    path('vehiclecategory/',VehicleCategoryView.as_view()),
    path('vehiclemodel/',VehicleModelView.as_view()),
    path('vehicledetails/',VehicleDetailsView.as_view()),

]
