from django.contrib import admin
from taxapp.models import *

admin.site.register(TaxMaster)  #register TaxMaster model

admin.site.register(FinancialYear)  #register FinancialYear model
