# Generated by Django 5.0.6 on 2024-07-08 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_job', '0004_rename_jobs_job_rename_address_application_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='Education_institute',
            new_name='education_institute',
        ),
    ]