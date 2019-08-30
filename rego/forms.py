from .models import Registration
from django import forms

class RegoForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email']

    def clean(self):
        email = self.cleaned_data['email']
        if not email.endswith('usc.edu.au'):
            raise ValidationError(
                    {'email': 'Must be a registered USC email address'}
            )
        if Registration.objects.filter(email=email):
            raise ValidationError(
                    {'email': 'Someone has already registered with this email address!'}
            )
        return self.cleaned_data
