from django.shortcuts import render
from .models import Snippet, Geolocator
from rest_framework import relations, response
from rest_framework.decorators import api_view
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCH
                     ListModelMixin):  # handles GETs for many Companies

	queryset = Company.objects.all()
	serializer_class = CompanySerializer


@api_view(['POST'])
def input_loc(request):

	def get_geoloc_data():
		pass


@api_view('GET')
def output_loc(request):
	pass
