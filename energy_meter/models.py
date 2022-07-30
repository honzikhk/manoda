from django.contrib.auth.models import User
from django.db import models


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.IntegerField()
    note = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return f"Date: {self.date} - value: {self.value}"

    class Meta:
        ordering = ["date"]
