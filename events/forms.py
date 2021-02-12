from django.core.exceptions import ValidationError
from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','short_description','description','photo']
        widgets = {
            'name': forms.TextInput(attrs={'class':'input-xlarge',}),
            'short_description': forms.TextInput(attrs={'class':'input-xlarge',}),
            'description':forms.Textarea(attrs={'class':'input-xlarge','rows':"5",}),
        }