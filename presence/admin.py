from django.contrib import admin
from .models import MarqueeMessage, Profile, Presence

# Register your models here.
admin.site.register(MarqueeMessage)
admin.site.register(Profile)
admin.site.register(Presence)
