from .models import Registration
from django import forms

class RegoForm(forms.ModelForm)
    class Meta:
        model = Registration
        fields = ['name', 'email']
