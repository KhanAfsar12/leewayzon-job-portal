from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_position = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)
    job_duration = models.CharField(max_length=200)
    job_sector = models.CharField(max_length=200)
    job_description = models.CharField(max_length=500)
    job_location = models.CharField(max_length=200)
    company_description = models.CharField(max_length=1000)
    responsibilities = models.CharField(max_length=500)
    qualification = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    skill = models.CharField(max_length=500)
    leewayzon_facility = models.CharField(max_length=1000)

    def __str__(self):
        return self.job_position


class Application(models.Model):
    form_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=200)

    experience_name = models.CharField(max_length=200)
    experience_company = models.CharField(max_length=200)
    experience_office_location = models.CharField(max_length=200)
    experience_description = models.CharField(max_length=500)
    experience_date_from = models.DateField(blank=True, null=True)
    experience_date_to = models.DateField(blank=True, null=True)

    education_institute = models.CharField(max_length=200)
    education_major = models.CharField(max_length=200)
    education_degree = models.CharField(max_length=200)
    education_school_location = models.CharField(max_length=200)
    education_description = models.CharField(max_length=500)
    education_date_from = models.DateField(blank=True, null=True)
    education_date_to = models.DateField(blank=True, null=True)

    linkedin_link = models.URLField(max_length=1000, blank=True, null=True)
    facebook_link = models.URLField(max_length=1000, blank=True, null=True)
    twitter_link = models.URLField(max_length=1000, blank=True, null=True)
    website_link = models.URLField(max_length=1000, blank=True, null=True)

    resume = models.FileField(upload_to='resumes/')

    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
