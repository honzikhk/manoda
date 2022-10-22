from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from energy_meter.forms import RecordForm
from energy_meter.models import Record


def count_avg_consumption():
    """ from all records counts amount of consumed electricity, days of measuring and average consumption per day """
    data = {}
    values_lst = Record.objects.values_list("value", flat=True)     # makes list of values
    max_value = max(values_lst)
    min_value = min(values_lst)
    dates_lst = Record.objects.values_list("date", flat=True)       # makes list of dates
    first_date = min(dates_lst)
    last_date = max(dates_lst)
    count_of_days_datetime = last_date - first_date

    consumed = max_value - min_value
    count_of_days_int = count_of_days_datetime.days
    avg_consumption = consumed / count_of_days_int
    price_per_month = round((13.9 * avg_consumption * 30))       # 13.9 is price pe kwh

    data["consumed"] = consumed
    data["count_of_days_int"] = count_of_days_int
    data["avg_consumption"] = round(avg_consumption, 2)
    data["price_per_month"] = price_per_month

    return data     # returns dictionary with data, that i need


def chart_consumption():
    data = {}
    avg_consumption_in_period_per_day = []
    periods = []
    days_between_measuring = []
    values_lst = Record.objects.values_list("value", flat=True)[::-1]     # makes list of values
    dates_lst = Record.objects.values_list("date", flat=True)[::-1]  # makes list of dates from the oldest record
    kw_in_period = []

    for i in range(len(dates_lst)):
        if i + 1 == len(dates_lst):
            break
        days_between_measuring.append(abs((dates_lst[i] - dates_lst[i + 1]).days))      # makes list of count days between measurements

    for i in range(len(dates_lst)):
        if i + 1 == len(dates_lst):
            break
        str_of_dates = dates_lst[i].strftime("%d.%m.%y")        # makes string from datetime (day.month.year)
        str_of_dates_next = dates_lst[i + 1].strftime("%d.%m.%y")       # makes string for next day
        periods.append(f"{str_of_dates} - {str_of_dates_next}")     # add string for axe X

    for i in range(len(values_lst)):
        if i + 1 == len(values_lst):
            break
        _ = values_lst[i + 1] - values_lst[i]       # diff between two measurements
        avg_consumption_in_period_per_day.append(round((_ / days_between_measuring[i]), 2))     # values for axe Y

    for i in range(len(values_lst) - 1):
        kw_in_period.append(values_lst[i + 1] - values_lst[i])
    

    data["periods"] = periods
    data["avg_consumption_in_period_per_day"] = avg_consumption_in_period_per_day
    data["days_between_measuring"] = days_between_measuring
    data["values_lst"] = values_lst
    data["number_of_values"] = len(values_lst)
    data["kw_in_period"] = kw_in_period

    return data
    # return f"periods: {periods}, avg_consumption_in_period_per_day: {avg_consumption_in_period_per_day}," \
    #        f" days_between_measuring: {days_between_measuring}, values_lst: {values_lst}"


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
            
            
            "chart_consumption": chart_consumption(),
        })
        return context

    def form_valid(self, form):  # this join created task to actual user
        form.instance.user = self.request.user
        return super(RecordCreateView, self).form_valid(form)


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy("energy_meter_base")
