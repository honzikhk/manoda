from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageTemplateView(TemplateView):
    template_name = "base/homepage.html"
