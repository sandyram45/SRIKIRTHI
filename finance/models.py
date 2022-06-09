from django.db import models
from django.utils import timezone


class DailyExpenses(models.Model):
    date = models.DateField(default=timezone.now)
    choices = [('STATIONARY', 'STATIONARY'), ('PETROL', 'PETROL'), ('EATERIES', 'EATERIES'), ('COMPUTER ACCESSORIES', 'COMPUTER ACCESSORIES')]
    expense = models.CharField(max_length=21, choices=choices, default='PETROL')
    description = models.CharField(max_length=30, blank=True)
    amount = models.PositiveIntegerField()


class VehicleExpenses(models.Model):
    date = models.DateField(default=timezone.now)
    choices = [('TN59BH0475', 'TN59BH0475')]
    vehicle_number = models.CharField(max_length=10, choices=choices)
    description = models.TextField()
    amount = models.PositiveIntegerField()


class SalaryExpenses(models.Model):
    date = models.DateField(default=timezone.now)
    person = [('SUNDARI', 'SUNDARI'), ('MUNIYANDI', 'MUNIYANDI'), ('GOPAL', 'GOPAL'), ('KUMAR', 'KUMAR'), ('RANJANI', 'RANJANGI'), ('OTHERS', 'OTHERS') ]
    persons = models.CharField(choices=person, max_length=10, default='GOPAL')
    amount = models.PositiveIntegerField()


