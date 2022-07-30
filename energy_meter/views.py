from django.shortcuts import render
from django.views.generic import ListView

from energy_meter.models import Record


class RecordListView(ListView):
    model = Record
    template_name = "energy_meter/energy_meter_base.html"

