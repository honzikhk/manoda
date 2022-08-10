from django.contrib.auth.models import User
from django.db import models


class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=200)
    note = models.TextField(null=True, blank=True)
    file = models.FileField()
