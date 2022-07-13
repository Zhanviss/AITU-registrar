from django.contrib import admin
from .models import Professor, ProfessorLinkPosition, JobPosition
# Register your models here.
admin.site.register(Professor)
admin.site.register(JobPosition)
admin.site.register(ProfessorLinkPosition)