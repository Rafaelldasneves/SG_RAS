from django import forms
from . import models


class PeriodForms(forms.ModelForm):

    class Meta:
        model = models.Period
        fields = ['name', 'date_start', 'date_end', 'description']
