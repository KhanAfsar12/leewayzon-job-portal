import pandas as pd
from django.core.management.base import BaseCommand

from auth_job.models import Job


class Command(BaseCommand):
    help = 'Upload jobs from an Excel file'

    def handle(self, *args, **kwargs):
        # Path to the Excel file
        file_path = 'C:\\Users\\hp\\Desktop\\kk.xlsx'
        
        # Read the Excel file
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            job = Job(
                job_position = row['Job Position'],
                job_type=row['Job Type'],
                job_duration=row['Job Duration'],
                job_sector=row['Job Sector'],
                job_description=row['Job Description'],
                job_location=row['Job Location'],
                company_description=row['Company Description'],
                responsibilities=row['Responsibilities'],
                qualification=row['Qualification'],
                experience=row['Experience'],
                skill=row['Skill'],
                leewayzon_facility=row['Leewayzon Facility']
            )
            job.save()

        self.stdout.write(self.style.SUCCESS('Successfully uploaded jobs from Excel file'))
