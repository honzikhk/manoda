from django.urls import path
from .views import RecordCreateView

urlpatterns = [
    path("energy_meter/base", RecordCreateView.as_view(), name="energy_meter_base"),

]
