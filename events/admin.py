from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    readonly_fields = ('slug', )
    

admin.site.register(Schedule)
admin.site.register(Event,EventAdmin)
admin.site.register(TheatreEvent)
admin.site.register(SportEvent)
admin.site.register(СoncertEvent)
admin.site.register(ExhibitionEvent)
admin.site.register(FilmEvent)
admin.site.register(NontypeEvent)
admin.site.register(Place)
admin.site.register(CinemaTheatre)
admin.site.register(Theatre)
admin.site.register(Showroom)
admin.site.register(СoncertHall)
admin.site.register(Restaurant) 
admin.site.register(NontypePlace)