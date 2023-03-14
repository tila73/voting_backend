from django import forms
# from ..main.models import *
from .models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'