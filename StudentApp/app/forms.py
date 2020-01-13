from django import forms        #forms is module & Form is a class.

class StudentForm(forms.Form):
    sname = forms.CharField()
    srn = forms.IntegerField()
    sclass = forms.CharField()
    smarks = forms.IntegerField()
