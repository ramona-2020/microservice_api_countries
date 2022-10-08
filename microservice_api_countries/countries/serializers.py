from rest_framework import serializers

from microservice_api_countries.countries.models import Country


# DRF serializers convert Django data types, such as querysets,
# into a format that can be rendered into JSON or XML.
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country     # this is the model that is being serialized
        fields = ('name', 'local_currency')
