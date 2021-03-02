from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework.serializers import ModelSerializer
from .models import Company, Geolocator


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id', 'name', 'description', 'website', 'street_line_1',
            'street_line_2', 'city', 'state', 'zipcode'
        )


class MainGeoSerializer(ModelSerializer):

    class Meta:
        model = Geolocator()
        fields = '__all__'
        read_only_fields = ['id', 'performed']


class OutputGeoSerializer(serializers.HyperlinkedModelSerializer):
    track_listing = serializers.HyperlinkedIdentityField(view_name='input_loc')

    class Meta:
        model = Geolocator()
        fields = '__all__'
