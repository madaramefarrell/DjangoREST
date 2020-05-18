from django.contrib import admin
from .models import beach


class BeachAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'location', 'lat', 'lng', 'created_at', 'update_at', 'status')


admin.site.register(beach.Beach, BeachAdmin)
