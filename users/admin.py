from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Location
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin),
admin.site.register(Location, LocationAdmin)