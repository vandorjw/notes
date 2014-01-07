from django.views import generic
from contact.models import Venue

class VenueListView(generic.ListView):
    queryset = Venue.objects.filter(is_active=True)

