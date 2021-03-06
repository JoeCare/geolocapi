from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Publisher, Author
from .serializers import BookSerializer, PublisherSerializer, AuthorSerializer
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
# from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

# Create your views here.


@api_view(['GET'])
def default(request):
    # return HttpResponse('default api view')
    return redirect('book-list-create')


class BookListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetailedView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class PublisherListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PublisherDetailedView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AuthorListView(generics.ListCreateAPIView):
# class AuthorListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


# mixins.RetrieveModelMixin,
class AuthorDetailedView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}

# class MultipleFieldLookupMixin:
#     """
#     Apply this mixin to any view or viewset to get multiple field filtering
#     based on a `lookup_fields` attribute, instead of the default single field filtering.
#     """
#     def get_object(self):
#         queryset = self.get_queryset()             # Get the base queryset
#         queryset = self.filter_queryset(queryset)  # Apply any filter backends
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs[field]: # Ignore empty fields.
#                 filter[field] = self.kwargs[field]
#         obj = get_object_or_404(queryset, **filter)  # Lookup the object
#         self.check_object_permissions(self.request, obj)
#         return obj

# def get_queryset(self):  # url ?q= querring method; first: from django.db.models import Q
#     qs = Book.objects.all()
#     query = self.request.GET.get("q")  # actual search
#     if query is not None:
#         qs = qs.filter(Q(title__icontains=query))
#         # qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
#     return qs

# class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_fields = ['account', 'username']

# def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)

# def list(self, request, *args, **kwargs):
#     queryset = self.filter_queryset(self.get_queryset())

#     page = self.paginate_queryset(queryset)
#     if page is not None:
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)

#     serializer = self.get_serializer(queryset, many=True)
#     return Response(serializer.data)
