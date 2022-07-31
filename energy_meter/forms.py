from django import forms
import datetime

from .models import Record


class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(CustomDateInput, self).__init__(*args, **kwargs)


class RecordForm(forms.ModelForm):
    date = forms.DateField(widget=CustomDateInput(), initial=datetime.date.today())

    class Meta:
        model = Record
        exclude = ["user"]  # there must be either "exclude" or "fields"
