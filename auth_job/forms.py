from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name', 'last_name', 'email', 'address', 'phone_number',
            'experience_name', 'experience_company', 'experience_office_location', 'experience_description', 'experience_date_from', 'experience_date_to',
            'education_institute', 'education_major', 'education_degree', 'education_school_location', 'education_description', 'education_date_from', 'education_date_to',
            'linkedin_link', 'facebook_link', 'twitter_link', 'website_link',
            'resume', 'message'
        ]
        widgets = {
            'experience_date_from': forms.DateInput(attrs={'type': 'date'}),
            'experience_date_to': forms.DateInput(attrs={'type': 'date'}),
            'education_date_from': forms.DateInput(attrs={'type': 'date'}),
            'education_date_to': forms.DateInput(attrs={'type': 'date'}),
        }