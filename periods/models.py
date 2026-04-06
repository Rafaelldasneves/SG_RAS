from django.db import models


class Period (models.Model):
    name = models.CharField (max_length=50, null=True, blank=True)
    date_start = models.DateField ()
    date_end = models.DateField ()
    description = models.CharField (max_length=100, null=True, blank=True)
    date_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_start']

    def __str__(self):
        return self.name