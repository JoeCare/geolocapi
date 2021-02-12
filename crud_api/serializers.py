from rest_framework import serializers
from .models import Book, Author, Publisher


class BookSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'pages_num',
                  'cover_image', 'publisher', 'authors']
        ready_only_fields = ['id']

    # def validate_title(self, _title):
    #     query = Book.objects.filter(title__iexact=_title)
    #     if self.instance:
    #         query = query.exclude(id=self.instance.id)
    #     if query.exists():
    #         raise serializers.ValidationError(
    #             'Title multiplication. Set unique title.')
    #     return _title


class AuthorSerializer(serializers.ModelSerializer):
    creations = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name',
                  'nickname', 'birthdate', 'books', 'creations']
        ready_only_fields = ['id']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']
        ready_only_fields = ['id']
