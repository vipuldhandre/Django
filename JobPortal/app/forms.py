from django import forms

class EngineeringForm(forms.Form):
    ejobs = forms.CharField()

class ManagementForm(forms.Form):
    mjobs = forms.CharField()

class OperationsForm(forms.Form):
    ojobs = forms.CharField()
