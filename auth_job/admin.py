import csv
import io
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from .models import Job, Application, Education, Experience
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, ChoiceDropdownFilter, DropdownFilter # type: ignore
from django.contrib.admin.filters import SimpleListFilter
from django_object_actions import DjangoObjectActions
from django.contrib.auth.models import User
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'phone_number', 'resume', 'linkedin_link', 'job_id',)
    search_fields = ('first_name', 'last_name', 'email', 'address', 'phone_number', 'resume', 'linkedin_link', )
    list_filter = (
                   ('address', DropdownFilter),
                   ('phone_number', ChoiceDropdownFilter),
                   ('user_id', RelatedDropdownFilter),
                   ('job_id', RelatedDropdownFilter),
                   
                   )
    actions = ['download_resume', 'custom_action']



    def download_resume(self, request, queryset):
        for application in queryset:
            filename = application.resume.name.split('/')[-1]
            response = HttpResponse(application.resume, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
        
    download_resume.short_description = 'Download selected resume'


    def custom_action(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="biodata.pdf"'

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        styles = getSampleStyleSheet()
        title_style = styles['Title']
        normal_style = styles['Normal']

        # Title
        elements.append(Paragraph("Biodata Document", title_style))
        elements.append(Paragraph("<br/>", normal_style))

        # Process each application
        for application in queryset:
            elements.append(Paragraph(f"Application for {application.first_name} {application.last_name}", title_style))
            elements.append(Paragraph("<br/>", normal_style))
            
            # Application Information
            application_info = [
                ('First Name', application.first_name),
                ('Last Name', application.last_name),
                ('Email', application.email),
                ('Address', application.address),
                ('Phone Number', application.phone_number),
                ('Resume', application.resume.url),
                ('LinkedIn Link', application.linkedin_link),
                ('Job ID', str(application.job_id))
            ]

            table = Table(application_info, colWidths=[2*inch, 4*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONT', (0, 1), (-1, -1), 'Helvetica'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0, 0), (-1, -1), 10),
                ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            elements.append(table)
            elements.append(Paragraph("<br/>", normal_style))

            # Experience Information
            experiences = application.user.experiences.all()
            for experience in experiences:
                elements.append(Paragraph(f"Experience at {experience.experience_company}", title_style))
                experience_info = [
                    ('Name', experience.experience_name),
                    ('Office Location', experience.experience_office_location),
                    ('Description', experience.experience_description),
                    ('Date From', str(experience.experience_date_from)),
                    ('Date To', str(experience.experience_date_to))
                ]
                table = Table(experience_info, colWidths=[2*inch, 4*inch])
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONT', (0, 1), (-1, -1), 'Helvetica'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 10),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                    ('TOPPADDING', (0, 0), (-1, -1), 5),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(table)
                elements.append(Paragraph("<br/>", normal_style))

            # Education Information
            educations = application.user.educations.all()
            for education in educations:
                elements.append(Paragraph(f"Education at {education.education_institute}", title_style))
                education_info = [
                    ('Major', education.education_major),
                    ('Degree', education.education_degree),
                    ('School Location', education.education_school_location),
                    ('Description', education.education_description),
                    ('Date From', str(education.education_date_from)),
                    ('Date To', str(education.education_date_to))
                ]
                table = Table(education_info, colWidths=[2*inch, 4*inch])
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONT', (0, 1), (-1, -1), 'Helvetica'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 10),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                    ('TOPPADDING', (0, 0), (-1, -1), 5),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(table)
                elements.append(Paragraph("<br/>", normal_style))

        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response

    custom_action.short_description = 'Download selected user data as PDF'
    

class EducationAdmin(admin.ModelAdmin):
    list_display = ('education_institute', 'education_major', 'education_degree', 'education_school_location', 'education_description', 'education_date_from', 'education_date_to', 'user',)
    search_fields = ('education_institute', 'education_major', 'education_degree', 'education_school_location', 'education_description', 'education_date_from', 'education_date_to',)
    list_filter = (
        ('education_institute', DropdownFilter),
        ('education_major', DropdownFilter),
        ('education_degree', DropdownFilter),
        ('education_school_location', DropdownFilter),
        ('education_description', DropdownFilter),
        ('education_date_to', DropdownFilter),
        ('user_id', RelatedDropdownFilter),
    )



class ExperienceAdmin(admin.ModelAdmin):
    
    list_display = ('experience_name', 'experience_company', 'experience_office_location', 'experience_description', 'experience_date_from', 'experience_date_to', 'user',)
    search_fields = ('experience_name', 'experience_company', 'experience_office_location', 'experience_description', 'experience_date_from', 'experience_date_to',)
    list_filter = (
        ('experience_name', DropdownFilter),
        ('experience_company', DropdownFilter),
        ('experience_office_location', DropdownFilter),
        ('experience_description', DropdownFilter),
        ('experience_date_from', DropdownFilter),
        ('experience_date_to', DropdownFilter),
        ('user_id', RelatedDropdownFilter),
    )



class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_position', 'job_type', 'job_duration', 'job_sector', 'job_description', 'job_location', 'company_description', 'responsibilities', 'qualification', 'experience', 'skill', 'leewayzon_facility', )
    search_fields = ('job_position', 'job_type', 'job_duration', 'job_sector', 'job_description', 'job_location', 'company_description', 'responsibilities', 'qualification', 'experience', 'skill',)
    list_filter = (
                    ('job_position', DropdownFilter),
                   ('job_type', DropdownFilter),
                   ('job_duration', DropdownFilter),
                   ('job_sector', DropdownFilter),
                   ('job_description', DropdownFilter),
                   )

    

class UserAdmin(admin.ModelAdmin):
    pass
    



admin.site.register(Application, ApplicationAdmin)
admin.site.register(Job, JobsAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
