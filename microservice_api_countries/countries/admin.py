from django.contrib import admin

from microservice_api_countries.countries.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'local_currency', 'created_on')
    search_fields = ('name', )
