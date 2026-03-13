from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    POSITION_CHOICES = [
        ('GCM', 'Guarda Civil Municipal'),
        ('GPCM', 'Guarda Patrimonial Civil Municipal'),
    ]

    position = models.CharField ('Cargo', max_length=5, choices=POSITION_CHOICES)
    username = models.CharField ("Nome de Guerra", max_length=20, unique=True)
    registration = models.CharField ("Matricula", max_length=5, unique=True)
    name = models.CharField ("Nome Completo", max_length=30)
    admission_date = models.DateField ("Data de Admissão",)
    email = models.EmailField("E-mail", blank=True, null=True)
    phone_number = models.CharField ("Telefone", max_length=15)

