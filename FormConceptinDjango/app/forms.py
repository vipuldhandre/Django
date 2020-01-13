from django import forms
from app.models import Book

class BookForm(forms.Form):
    bname=forms.CharField()
    bauthor=forms.CharField()
    bprice=forms.IntegerField()

    def clean_bname(self):
        name=self.cleaned_data.get('bname')
        if name=="Java":
            raise forms.ValidationError("Java is not good.")
        return name
# user creation form

class UserCreationForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=[
            'bname',
            'bauthor',
            'bprice',
        ]
