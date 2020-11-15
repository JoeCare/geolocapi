from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Publisher, Author
from .serializers import BookSerializer, PublisherSerializer, AuthorSerializer
from rest_framework import generics, mixins


# from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,
# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin DestroyModelMixin
# Create your views here.


def default(request):
    # return HttpResponse('default api view')
    return redirect('book-list-create')

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


class BookListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetailedView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = BookSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    queryset = Book.objects.all()

    # def get_queryset(self):
    #     return Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PublisherListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# mixins.RetrieveModelMixin,
class PublisherDetailedView(generics.RetrieveAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AuthorListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthorDetailedView(generics.RetrieveAPIView):  # mixins.RetrieveModelMixin,
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
