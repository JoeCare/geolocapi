from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpRequest
import requests, os
from rest_framework.authentication import get_authorization_header
from rest_framework import relations, response, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from .models import Company, Geolocator, Snippet
from .serializers import (UserSerializer, CompanySerializer, MainGeoSerializer, OutputGeoSerializer)
from rest_framework_simplejwt.authentication import JWTAuthentication as jwt


class CompanyViewSet(viewsets.GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCH
                     ListModelMixin):  # handles GETs for many Companies

	queryset = Company.objects.all()
	serializer_class = CompanySerializer


@api_view(['POST', 'GET'])
def input_loc(request):
	# queryset = Geolocator.objects.all()
	# serializer_class = MainGeoSerializer
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
			print(data1.json())
			return HttpResponse(data1.json())
		else:
			data2 = requests.get(
				f"http://api.ipstack.com/check?access_key="
				f"{os.getenv('ipstackKey')}"
				f"&security=1&hostname=1")
			# print(data2.json())
			return response.Response(data2.json())

	# if request.method == 'POST':


class UserViewSet(viewsets.ModelViewSet, jwt):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = [jwt]

	def get_authenticators(self):
		auth_head = get_authorization_header(self.request)
		ah = jwt.get_header(self, request=self.request)

		token = jwt.get_raw_token(self, header=auth_head)

		return [auth() for auth in self.authentication_classes]

	def get_permissions(self):
		if self.action == 'list':
			permission_classes = [permissions.IsAuthenticated]
		else:
			permission_classes = [permissions.IsAdminUser]

		return [permission() for permission in permission_classes]


class LocationsViewSet(viewsets.ViewSet):
	"""Simplest viewset for list and detailed view"""

	def list(self, request):
		queryset = Geolocator.objects.all()
		serializer = MainGeoSerializer(queryset, many=True)
		return response.Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Geolocator.objects.all()
		location = get_object_or_404(queryset, pk=pk)
		serializer = MainGeoSerializer(location)
		return response.Response(serializer.data)

	def create(self, request):
		pass


class LocationsModelViewSet(viewsets.ModelViewSet):
	"""ModelViewSet with all """

	serializer_class = MainGeoSerializer
	queryset = Geolocator.objects.all()

	if MainGeoSerializer has


	# def get_serializer_context(self):
	def get_permissions(self):
		"""Sets list of permissions needed on this view's actions"""

		if self.action == 'list':
			permission_classes = [permissions.AllowAny]
		elif self.action == 'create':
			permission_classes = [permissions.IsAdminUser]
		else:
			permission_classes = [permissions.IsAuthenticated]

		return [permission() for permission in permission_classes]


# class Locations
