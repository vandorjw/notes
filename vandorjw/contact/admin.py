from django.contrib import admin
from contact.models import Venue

class VenueAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'is_active',
        'sort',
    )

admin.site.register(Venue, VenueAdmin)
