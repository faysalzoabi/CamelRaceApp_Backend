from django.contrib import admin
from .models import UserProfile, Camel, Season, Event
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Camel)
admin.site.register(Season)
admin.site.register(Event)
