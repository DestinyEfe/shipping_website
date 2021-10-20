from django.urls import path

from .views import IndexView, AboutView, ServicesView, GeneralTermsView, TrackCodeSearchView, TrackAndTraceView, GetFreeQuote, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('general_terms/', GeneralTermsView.as_view(), name='terms'),
    path('track_and_trace/', TrackCodeSearchView.as_view(), name='track_search'),
    path('track_results/', TrackAndTraceView.as_view(), name='track'),
    path('get_free_quote', GetFreeQuote.as_view(), name='quote'),
    path('contact/', ContactView.as_view(), name='contact'),
    
]