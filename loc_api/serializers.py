from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework.serializers import ModelSerializer
from .models import Geolocator
from django.contrib.auth.models import User




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','password', 'email']
        # fields = '__all__'


class MainGeoSerializer(ModelSerializer):

    class Meta:
        model = Geolocator
        fields = '__all__'
        # read_only_fields = ['id', 'performed']


class OutputGeoSerializer(serializers.HyperlinkedModelSerializer):
    input_locin = serializers.HyperlinkedIdentityField(view_name='input_loc')

    class Meta:
        model = Geolocator
        fields = '__all__'
