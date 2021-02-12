from django.core.exceptions import ValidationError
from .models import News
from django import forms

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['headline','text','photo','category']
        widgets = {
            'headline': forms.TextInput(attrs={'class':'input-xlarge',}),
            'text':forms.Textarea(attrs={'class':'input-xlarge','rows':"5",}),
            'category':forms.Select(attrs={'class':'form-control',})
        }