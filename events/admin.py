from django.contrib import admin
from .models import Venue
from .models import MyclubUser
from .models import Event

admin.site.register(Venue)
admin.site.register(MyclubUser)
admin.site.register(Event)

