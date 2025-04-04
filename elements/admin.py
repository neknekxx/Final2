from django.contrib import admin
from .models import Element
from .models import Discovery

admin.site.register(Element)

class DiscoveryAdmin(admin.ModelAdmin):
    list_display = ('element_name', 'discovered_by', 'discovery_year', 'trivia')
    
admin.site.register(Discovery, DiscoveryAdmin)