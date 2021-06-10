from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'Shipper/index.html'

class AboutView(TemplateView):
    template_name = 'Shipper/about.html'

class ServicesView(TemplateView):
    template_name = 'Shipper/services.html'

class GeneralTermsView(TemplateView):
    template_name = 'Shipper/general_terms.html'

class TrackAndTraceView(TemplateView):
    template_name = 'Shipper/track_and_trace.html'

class GetFreeQuote(TemplateView):
    template_name = 'Shipper/quote.html'

class ContactView(TemplateView):
    template_name = 'Shipper/contact.html'
