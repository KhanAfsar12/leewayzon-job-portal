import csv
import io
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from .models import Job, Application, Education, Experience
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, ChoiceDropdownFilter, DropdownFilter # type: ignore
from django.contrib.admin.filters import SimpleListFilter
from django_object_actions import DjangoObjectActions # type: ignore
from django.contrib.auth.models import User
from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph # type: ignore
from reportlab.lib.units import inch # type: ignore
from reportlab.lib import colors # type: ignore
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # type: ignore


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
        wrap_style = ParagraphStyle(name='Wrap', wordWrap='CJK')

        # Title
        elements.append(Paragraph("<br/>", normal_style))

        # Process each application
        for application in queryset:
            elements.append(Paragraph(f"Application for {application.first_name} {application.last_name}", title_style))
            elements.append(Paragraph("<br/>", normal_style))
            
            # Application Information
            application_info = [
                ('First Name', Paragraph(application.first_name, wrap_style)),
                ('Last Name', Paragraph(application.last_name, wrap_style)),
                ('Email', Paragraph(application.email, wrap_style)),
                ('Address', Paragraph(application.address, wrap_style)),
                ('Phone Number', Paragraph(application.phone_number, wrap_style)),
                ('Resume', Paragraph(application.resume.url, wrap_style)),
                ('LinkedIn Link', Paragraph(application.linkedin_link, wrap_style)),
                ('Job ID', Paragraph(str(application.job_id), wrap_style))
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
            elements.append(Paragraph("<br/> <br/> <br/>", normal_style))




            # Experience Information
            experiences = application.user.experiences.all()
            if experiences:
                elements.append(Paragraph("Experience Information", title_style))
                experience_data = [['Company', 'Name', 'Office Location', 'Description', 'Date From', 'Date To']]
                for experience in experiences:
                    experience_data.append([
                        Paragraph(experience.experience_company,wrap_style),
                        Paragraph(experience.experience_name,wrap_style),
                        Paragraph(experience.experience_office_location,wrap_style),
                        Paragraph(experience.experience_description, wrap_style),
                        Paragraph(str(experience.experience_date_from), wrap_style),
                        Paragraph(str(experience.experience_date_to), wrap_style)
                    ])

                table = Table(experience_data, colWidths=[1.7*inch, 1.5*inch, 1.5*inch, 1.5*inch, 1*inch, 1*inch])
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONT', (0, 0), (0, 0), 'Helvetica-Bold'),
                    ('FONT', (0, 1), (-1, -1), 'Helvetica'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 10),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                    ('TOPPADDING', (0, 0), (-1, -1), 5),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(table)
                elements.append(Paragraph("<br/> <br/> <br/> ", normal_style))




            # Education Information
            educations = application.user.educations.all()
            if educations:
                elements.append(Paragraph("Education Information", title_style))
                education_data = [['Institute', 'Major', 'Degree', 'School Location', 'Description', 'Date From', 'Date To']]
                for education in educations:
                    education_data.append([
                        Paragraph(education.education_institute, wrap_style),
                        Paragraph(education.education_major, wrap_style),
                        Paragraph(education.education_degree, wrap_style),
                        Paragraph(education.education_school_location, wrap_style),
                        Paragraph(education.education_description, wrap_style),
                        Paragraph(str(education.education_date_from), wrap_style),
                        Paragraph(str(education.education_date_to), wrap_style)
                    ])

                table = Table(education_data, colWidths=[1.5*inch,1*inch, 1*inch, 1.3*inch, 1.5*inch, 1*inch])
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONT', (0, 0), (0, 0), 'Helvetica-Bold'),
                    ('FONT', (0, 1), (-1, -1), 'Helvetica'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 10),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                    ('TOPPADDING', (0, 0), (-1, -1), 5),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(table)
                elements.append(Paragraph("<br/> <br/> <br/> ", normal_style))

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
