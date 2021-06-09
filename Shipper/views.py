from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'Shipper/index.html'

class AboutView(TemplateView):
    template_name = 'Shipper/about.html'
