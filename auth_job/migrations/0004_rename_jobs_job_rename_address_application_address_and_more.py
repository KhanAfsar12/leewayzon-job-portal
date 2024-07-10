# Generated by Django 5.0.6 on 2024-07-08 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_job', '0003_alter_application_job_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Education_date_from',
            new_name='education_date_from',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Education_date_to',
            new_name='education_date_to',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Education_Degree',
            new_name='education_degree',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Education_description',
            new_name='education_description',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Education_Major',
            new_name='education_major',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Education_school_location',
            new_name='education_school_location',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Experience_company',
            new_name='experience_company',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Experience_date_from',
            new_name='experience_date_from',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Experience_date_to',
            new_name='experience_date_to',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Experience_description',
            new_name='experience_description',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Experience_name',
            new_name='experience_name',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Experience_office_location',
            new_name='experience_office_location',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Facebook_link',
            new_name='facebook_link',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Form_id',
            new_name='form_id',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='job_id',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='LinkedIn_link',
            new_name='linkedin_link',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Resume',
            new_name='resume',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Twitter_link',
            new_name='twitter_link',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Website_link',
            new_name='website_link',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Company_description',
            new_name='company_description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Experience',
            new_name='experience',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_description',
            new_name='job_description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_duration',
            new_name='job_duration',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_id',
            new_name='job_id',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_location',
            new_name='job_location',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_position',
            new_name='job_position',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_sector',
            new_name='job_sector',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_type',
            new_name='job_type',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Leewayzon_facility',
            new_name='leewayzon_facility',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Qualification',
            new_name='qualification',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Responsibilities',
            new_name='responsibilities',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Skill',
            new_name='skill',
        ),
    ]
