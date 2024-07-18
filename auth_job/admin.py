from django.contrib import admin
from django.http import HttpResponse
from .models import Job, Application
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, ChoiceDropdownFilter,SimpleDropdownFilter, DropdownFilter # type: ignore
from django.contrib.admin.filters import SimpleListFilter

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'phone_number', 'resume', 'linkedin_link', 'experience_name', 'job_id',)
    search_fields = ('first_name', 'last_name', 'email', 'address', 'phone_number', 'resume', 'linkedin_link', 'experience_name',)
    list_filter = (
                    ('experience_name', DropdownFilter),
                   ('address', DropdownFilter),
                   ('phone_number', ChoiceDropdownFilter),
                   ('user_id', RelatedDropdownFilter),
                   ('job_id', RelatedDropdownFilter),
                   
                   )
    actions = ['download_resume']



    def download_resume(self, request, queryset):
        for application in queryset:
            filename = application.resume.name.split('/')[-1]
            response = HttpResponse(application.resume, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
        
    download_resume.short_description = 'Download selected resume'

    


class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_position', 'job_type', 'job_duration', 'job_sector', 'job_description', 'job_location', 'company_description', 'responsibilities', 'qualification', 'experience', 'skill', 'leewayzon_facility', )
    search_fields = ('job_position', 'job_type', 'job_duration', 'job_sector', 'job_description', 'job_location', 'company_description', 'responsibilities', 'qualification', 'experience', 'skill', 'leewayzon_facility', )
    list_filter = (
                    ('job_position', DropdownFilter),
                   ('job_type', DropdownFilter),
                   ('job_duration', DropdownFilter),
                   ('job_sector', DropdownFilter),
                   ('job_description', DropdownFilter),
                   )

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Job, JobsAdmin)