from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from energy_meter.forms import RecordForm
from energy_meter.models import Record


def count_avg_consumption():
    """ from all records counts amount of consumed electricity, days of measuring and average consumption per day """
    data = {}
    max_value = max(Record.objects.values_list("value", flat=True))
    min_value = min(Record.objects.values_list("value", flat=True))
    consumed = max_value - min_value
    first_date = min(Record.objects.values_list("date", flat=True))
    last_date = max(Record.objects.values_list("date", flat=True))
    count_of_days_datetime = last_date - first_date
    count_of_days_int = count_of_days_datetime.days
    avg_consumption = consumed / count_of_days_int
    price_per_month = round((8.5 * avg_consumption * 30))

    data["consumed"] = consumed
    data["count_of_days_int"] = count_of_days_int
    data["avg_consumption"] = round(avg_consumption, 2)
    data["price_per_month"] = price_per_month
    return data


class RecordCreateView(CreateView):
    model = Record
    template_name = "energy_meter/energy_meter_base.html"
    form_class = RecordForm

    # this makes possible to iterate through records in template
    def get_context_data(self, **kwargs):
        context = super(RecordCreateView, self).get_context_data(**kwargs)
        context.update({
            "records": Record.objects.all(),
            "consumed": count_avg_consumption()["consumed"],
            "number_of_days": count_avg_consumption()["count_of_days_int"],
            "avg_consumption": count_avg_consumption()["avg_consumption"],
            "price_per_month": count_avg_consumption()["price_per_month"],
        })
        return context

    def form_valid(self, form):  # this join created task to actual user
        form.instance.user = self.request.user
        return super(RecordCreateView, self).form_valid(form)


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy("energy_meter_base")
