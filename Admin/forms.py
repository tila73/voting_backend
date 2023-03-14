from django import forms
# from ..main.models import *
from .models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class CountsForm(forms.ModelForm):
    class Meta:
        model = Counts
        fields = '__all__'
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
class WhyChooseUsForm(forms.ModelForm):
    class Meta:
        model = WhyChooseUs
        fields = '__all__'
class TeamsForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = '__all__'

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

class faqForm(forms.ModelForm):
    class Meta:
        model = faq
        fields = '__all__'
class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'