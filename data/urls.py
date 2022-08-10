from django.urls import path
from .views import DataCreateView

urlpatterns = [
    path("data_base/", DataCreateView.as_view(), name="data_base"),
]
