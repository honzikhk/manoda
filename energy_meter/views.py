from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView

from energy_meter.forms import RecordForm
from energy_meter.models import Record


class RecordCreateView(CreateView):
    model = Record
    template_name = "energy_meter/energy_meter_base.html"
    form_class = RecordForm

    # this make possible to iterate through records in template
    def get_context_data(self, **kwargs):
        context = super(RecordCreateView, self).get_context_data(**kwargs)
        context.update({
            "records": Record.objects.all(),
        })
        return context

    def form_valid(self, form):  # this join created task to actual user
        form.instance.user = self.request.user
        return super(RecordCreateView, self).form_valid(form)


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy("energy_meter_base")
