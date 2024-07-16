from django.contrib import admin

from .models import Car, Part, Country

admin.site.register(Car)
admin.site.register(Part)
admin.site.register(Country)
