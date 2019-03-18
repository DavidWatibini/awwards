from django import forms
from .models import *

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('website',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('website',)
