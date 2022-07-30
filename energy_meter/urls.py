from django.urls import path
from . import views
from .views import RecordListView

urlpatterns = [
    path("energy_meter/base", RecordListView.as_view(), name="energy_meter_base"),
]
