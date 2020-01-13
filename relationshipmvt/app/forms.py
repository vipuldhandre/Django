from django.forms import ModelForm
from app.models import (Company,Languages,Programmer)

class ProgrammerForm(ModelForm):
    class Meta:
        model = Programmer
        fields = '__all__' # or ['pname','company','languages']
