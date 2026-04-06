from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('period', 'date', 'time_start', 'time_end', 'vacancies', 'remaining_vacancies')
    list_filter = ('period', 'date')