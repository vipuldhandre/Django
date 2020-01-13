from django.forms import ModelForm
from taxapp.models import TaxMaster,FinancialYear
from django import forms

class TaxMasterForm(ModelForm):
    class Meta:
        model = TaxMaster
        fields = "__all__"

class FinancialYearForm(ModelForm):
    class Meta:
        model = FinancialYear
        fields = "__all__"
        widgets = {
            "fin_date_from":forms.DateInput(attrs={'type':'date'}),
            "fin_date_to":forms.DateInput(attrs={'type':'date'}),

        }
