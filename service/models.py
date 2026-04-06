from django.db import models
from periods.models import Period


class Service(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='plantoes',)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    vacancies = models.IntegerField()

    class Meta:
        ordering = ['date', 'time_start']
        unique_together = ('period', 'date', 'time_start')

    def __str__(self):
        return f"{self.period.name} - {self.date.strftime('%d/%m/%Y')} - {self.time_start.strftime('%H:%M')}"

    @property
    def occupied_vacancies(self):
        return self.registrations.filter(status='CONFIRMADO').count()

    @property
    def remaining_vacancies(self):
        return self.vacancies - self.occupied_vacancies

    @property
    def reservation_list(self):
        return self.registrations.filter(status='RESERVA').order_by('date_vacancie')