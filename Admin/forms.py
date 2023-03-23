from django import forms
# from ..main.models import *
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


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

class TeamMemberForm(forms.ModelForm):
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
        

class NewsDetailsForm(forms.ModelForm):
    class Meta:
        model = NewsDetails
        fields = '__all__'


class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = '__all__'


class AboutDetailsForm(forms.ModelForm):
    class Meta:
        model = AboutDetails
        fields = '__all__'
        

class TestimonialDetailsForm(forms.ModelForm):
    class Meta:
        model = TestimonialDetails
        fields = '__all__'


class blogDetailsForm(forms.ModelForm):
    class Meta:
        model = blogDetails
        fields = '__all__'

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
class faqAnsForm(forms.ModelForm):
    class Meta:
        model = faq
        fields = ['question', 'answer']
