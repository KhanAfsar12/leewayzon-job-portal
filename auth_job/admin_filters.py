from django.contrib import admin
from django.db.models import Count
from .models import Application

class ExperienceNameDropdownFilter(admin.FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Application.objects.values_list('experience_name', 'experience_name').distinct()

    def expected_parameters(self):
        return [self.field_path]

    def choices(self, changelist):
        return self.lookup_choices, []

class AddressDropdownFilter(admin.FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Application.objects.values_list('address', 'address').distinct()

    def expected_parameters(self):
        return [self.field_path]

    def choices(self, changelist):
        return self.lookup_choices, []

class PhoneNumberDropdownFilter(admin.FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Application.objects.values_list('phone_number', 'phone_number').distinct()

    def expected_parameters(self):
        return [self.field_path]

    def choices(self, changelist):
        return self.lookup_choices, []

class UserDropdownFilter(admin.FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Application.objects.values_list('user__id', 'user__username').distinct()

    def expected_parameters(self):
        return [self.field_path]

    def choices(self, changelist):
        return self.lookup_choices, []
