# Generated by Django 5.0.6 on 2024-07-08 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='auth_job.jobs'),
        ),
    ]
