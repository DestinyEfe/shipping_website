from django.db.models import query
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from Shipper.models import Package
# Create your views here.

posts = [
    {
        'id': 0,
        'name': 'Destiny',
    },
     {
        'id': 1,
        'name': 'Victory',
    }
]

class IndexView(TemplateView):
    template_name = 'Shipper/index.html'

class AboutView(TemplateView):
    template_name = 'Shipper/about.html'

class ServicesView(TemplateView):
    template_name = 'Shipper/services.html'

class GeneralTermsView(TemplateView):
    template_name = 'Shipper/general_terms.html'


class TrackCodeSearchView(TemplateView):
    template_name = 'Shipper/tracK_and_trace.html'

class TrackAndTraceView(ListView):
    model = Package
    template_name = 'Shipper/track_and_trace.html'
    context_object_name = 'packages'
    

    def get_queryset(self):
        query = self.request.GET.get('tracking_code')
        object = Package.objects.filter(tracking_code__startswith=query)
        
        return object
        

class GetFreeQuote(TemplateView):
    template_name = 'Shipper/quote.html'

class ContactView(TemplateView):
    template_name = 'Shipper/contact.html'
