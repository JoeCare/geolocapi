from django.shortcuts import render
import requests, os
from rest_framework import relations, response
from rest_framework.decorators import api_view
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .models import Company, Geolocator, Snippet
from .serializers import CompanySerializer, MainGeoSerializer, OutputGeoSerializer


class CompanyViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCH
                     ListModelMixin):  # handles GETs for many Companies

	queryset = Company.objects.all()
	serializer_class = CompanySerializer


@api_view(['POST', 'GET'])
def input_loc(request):
	queryset = Geolocator.objects.all()
	serializer_class = OutputGeoSerializer
	"""
	if POST then sending ip and storing in db
	if GET sends def check and owc location 
	"""
	if request.method == 'GET':
		# def get_geoloc_data():
		locator = Geolocator(input_ipv4=request.body)
		if locator.input_ipv4:
			data1 = requests.get(
				f"http://api.ipstack.com/{locator.input_ipv4}?access_key="
				f"{os.getenv('ipstackKey')}"
				f"&security=1&hostname=1")
			return response.Response(data1.json())
		else:
			data2 = requests.get(
				f"http://api.ipstack.com/check?access_key="
				f"{os.getenv('ipstackKey')}"
				f"&security=1&hostname=1")
			return response.Response(data2.json())


@api_view(['GET'])
def output_loc(request):
	pass
