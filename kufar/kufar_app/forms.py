from django import forms
from .models import *

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'status', 'description', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['name', 'model', 'status', 'description', 'price']

class PhoneImageForm(forms.ModelForm):
    class Meta:
        model = PhoneImage
        fields = ['images']

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['name', 'model', 'status', 'description', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = ['name', 'model', 'status', 'description', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

