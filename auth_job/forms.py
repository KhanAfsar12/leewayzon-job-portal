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
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'experience_name': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_company': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_office_location': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'experience_date_from': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'experience_date_to': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'education_institute': forms.TextInput(attrs={'class': 'form-control'}),
            'education_major': forms.TextInput(attrs={'class': 'form-control'}),
            'education_degree': forms.TextInput(attrs={'class': 'form-control'}),
            'education_school_location': forms.TextInput(attrs={'class': 'form-control'}),
            'education_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'education_date_from': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'education_date_to': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'website_link': forms.URLInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }