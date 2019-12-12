from django import forms


class EmployeeForm(forms.Form):
        #eid = forms.AutoField(primary_key=True)
        ename = forms.CharField(max_length=30)
        edes = forms.CharField(max_length=30)
        esal = forms.FloatField()
