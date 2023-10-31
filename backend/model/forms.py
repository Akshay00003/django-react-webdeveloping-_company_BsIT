from django import forms
from .models import Appoinment

class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields  = '__all__'
        labels = {
            'name' : 'NAME',
            'phone' : 'CONTACT NO',
            'email' : 'EMAIL',
            
        }