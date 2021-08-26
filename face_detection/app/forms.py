from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerFormImage(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('image',)

