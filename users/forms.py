from django import forms
from django.contrib.auth.models import User
from .models import Location, Profile


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name'}

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = {'photo', 'bio', 'phone_number'}

class LocationForm(forms.ModelForm):
    class Meta:
        address_1 = forms.CharField(required=True)
        zip_code = forms.CharField(required=True)
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'}