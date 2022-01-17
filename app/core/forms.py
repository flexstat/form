from django import forms
from .models import FeedBackMain

class ContactForm(forms.ModelForm):

    class Meta:
        model = FeedBackMain
        fields = ['domain_name', 'description', 'name','email','phone','inform']
       