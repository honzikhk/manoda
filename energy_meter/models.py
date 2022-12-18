from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import resolve_url


class Record(models.Model):     # maybe better name will be EnergyMeterRecord
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.IntegerField()

    def __str__(self):
        return f"Date: {self.date} - value: {self.value}"

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        return resolve_url("energy_meter_base")



