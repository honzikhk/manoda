from django.shortcuts import render
from django.views.generic import ListView, CreateView

from energy_meter.forms import RecordForm
from energy_meter.models import Record


class RecordListView(ListView):
    model = Record
    template_name = "energy_meter/energy_meter_base.html"


class RecordCreateView(CreateView):
    model = Record
    template_name = "energy_meter/energy_meter_base.html"
    form_class = RecordForm

    def get_queryset(self):
        records = Record.objects.all()
