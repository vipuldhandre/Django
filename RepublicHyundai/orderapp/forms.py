from orderapp.models import Order,OrderDetails
from django.forms import ModelForm
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            "order_date":forms.DateInput(attrs={'type':'date'}),
        }

class OrderDetailsForm(ModelForm):
    class Meta:
        model = OrderDetails
        fields = "__all__"
