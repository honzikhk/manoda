from django import forms
from .models import Data


class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        exclude = ["user", "date"]  # there must be either "exclude" or "fields"