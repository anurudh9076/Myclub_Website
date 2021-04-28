from django import forms
from django.forms import ModelForm
from .models import Venue

#create a venue form 

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        #field = "__all__"
        fields = ('name', 'address', 'zip_code','phone','web','email_adress')
        labels ={
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_adress':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':' venue name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'venue address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'zip code'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'web': forms.TextInput(attrs={'class':'form-control','placeholder':'website'}),
            'email_adress':forms.EmailInput(attrs={'class':'form-control','placeholder':'email address'}),
        }
