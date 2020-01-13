from django.urls import path
from taxapp.views import TaxMasterView,FinancialYearView


urlpatterns = [

    path('taxmaster/',TaxMasterView.as_view()),
    path('financialyear/',FinancialYearView.as_view()),

]
