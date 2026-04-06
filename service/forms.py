from django import forms
from . import models


class ServiceForms(forms.ModelForm):

    class Meta:
        model = models.Service
        fields = [ 'period', 'date', 'time_start', 'time_end', 'vacancies',]