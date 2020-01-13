from django.forms import ModelForm
from servicesapp.models import LabourDetails,LabourOperationMaster,RoDetails,RoPartDetails
from django import forms

class LabourDetailsForm(ModelForm):
    class Meta:
        model = LabourDetails
        fields = "__all__"

class LabourOperationMasterForm(ModelForm):
    class Meta:
        model = LabourOperationMaster
        fields = "__all__"

class RoDetailsForm(ModelForm):
    class Meta:
        model = RoDetails
        fields = "__all__"
        widgets ={
            "ro_received_date":forms.DateInput(attrs={'type':'date'}),
            "ro_received_time":forms.TimeInput(attrs={'type':'time'}),
            "ro_open_date":forms.DateInput(attrs={'type':'date'}),
            "ro_open_time":forms.TimeInput(attrs={'type':'time'}),
            "ro_closed_date":forms.DateInput(attrs={'type':'date'}),
            "ro_closed_time":forms.TimeInput(attrs={'type':'time'}),
            "ro_promise_date":forms.DateInput(attrs={'type':'date'}),
            "ro_promise_time":forms.TimeInput(attrs={'type':'time'}),

        }

class RoPartDetailsForm(ModelForm):
    class Meta:
        model = RoPartDetails
        fields = "__all__"
