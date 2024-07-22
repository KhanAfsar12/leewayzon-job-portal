from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application, Education, Experience
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
            'linkedin_link', 'facebook_link', 'twitter_link', 'website_link',
            'resume', 'message'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'website_link': forms.URLInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }



class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'education_institute', 'education_major', 'education_degree', 'education_school_location', 'education_description', 'education_date_from', 'education_date_to'
        ]

        widgets ={ 
            'education_description': forms.Textarea(attrs={'class': 'form-control', 'rows':2}),
            'education_date_from': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'education_date_to': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            'experience_name', 'experience_company', 'experience_office_location', 'experience_description', 'experience_date_from', 'experience_date_to'
        ]

        widgets = {
            'experience_description': forms.Textarea(attrs={'class': 'form-control', 'rows':2}),
            'experience_date_from': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'experience_date_to': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



EducationFormSet = forms.modelformset_factory(Education, form=EducationForm, extra=1)
ExperienceFormSet = forms.modelformset_factory(Experience, form=ExperienceForm, extra=1)