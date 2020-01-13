from django.urls import path
from servicesapp.views import LabourDetailsView,LabourOperationMasterView,RoDetailsView,RoPartDetailsView

urlpatterns = [

    path('labourdetails/',LabourDetailsView.as_view()),
    path('labouroperationmaster/',LabourOperationMasterView.as_view()),
    path('rodetails/',RoDetailsView.as_view()),
    path('ropartdetails/',RoPartDetailsView.as_view()),

]
