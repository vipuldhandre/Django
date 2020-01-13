from app.models import Test
from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets

class TestForm(forms.ModelForm):
    #dob = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)
    class Meta:
        model = Test
        fields = "__all__"
        widgets = {
            "dob":forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
