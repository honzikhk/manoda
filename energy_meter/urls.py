from django.urls import path
from .views import RecordCreateView, RecordDeleteView

urlpatterns = [
    path("energy_meter_base/", RecordCreateView.as_view(), name="energy_meter_base"),
    path("record_delete/<int:pk>/", RecordDeleteView.as_view(), name="delete_record"),

]
