from django import forms
from .models import *

class questionForm(forms.ModelForm):
    class Meta:
        model = faq
        fields = ['name', 'email', 'question']