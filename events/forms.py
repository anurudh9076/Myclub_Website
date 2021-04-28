from django import forms
from django.forms import ModelForm
from .models import Venue,Event

#create a venue form 
class EventForm(ModelForm):
    class Meta:
        model = Event
        #field = "__all__"
        fields = ('name', 'event_date', 'venue','manager','description','attendees')
        labels ={
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM',
            'venue': 'Venue',
            'manager': 'Manager',
            'description': '',
            'attendees':'Attendees',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':' name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'event date'}),
            'venue': forms.Select(attrs={'class':'form-select','placeholder':'venue'}),
            'manager': forms.Select(attrs={'class':'form-select','placeholder':'manager'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'description'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'attendees'}),
        }


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
