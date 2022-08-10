from django.shortcuts import render
from django.views.generic import CreateView

from .forms import DataForm
from .models import Data


class DataCreateView(CreateView):
    model = Data
    template_name = "data/data_base.html"
    form_class = DataForm

