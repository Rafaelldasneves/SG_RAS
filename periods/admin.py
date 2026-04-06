from django.contrib import admin
from .models import Period

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end', 'description')
    search_fields = ('name', 'description')