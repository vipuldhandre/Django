from django import forms
from app.models import *

class ProfileForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields=[
                'name',
                'propic',
                
        ]
