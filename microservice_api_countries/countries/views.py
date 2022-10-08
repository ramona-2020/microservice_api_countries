from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Country
from .serializers import CountrySerializer


@api_view(['GET', 'POST'])
def show_countries(request):
    countries = Country.objects.values()
    countries_list = [{'name': c["name"], 'local_currency': c["local_currency"]} for c in countries]

    if request.method == 'GET':
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CountrySerializer(data=request.data)

        if request.data in countries_list:
            return Response("Country already exists", status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def country_details(request, pk):
    try:
        country = Country.objects.get(pk=pk)

        serializer = CountrySerializer(country)
        return Response(serializer.data)
    except Country.DoesNotExist:
        return Response("Country not found", status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def country_update(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Country.DoesNotExist:
        return Response("Country not found", status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def country_delete(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response(status=status.HTTP_200_OK)
    except Country.DoesNotExist:
        return Response("Country not found", status=status.HTTP_404_NOT_FOUND)
