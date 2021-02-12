from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('api01/auth/', include('rest_framework.urls')),
    path('api01/books/<int:id>', views.BookDetailedView.as_view(), name='book-rud'),
    path('api01/books/', views.BookListView.as_view(), name='book-list-create'),
    path('api01/publishers/<int:id>',
         views.PublisherDetailedView.as_view(), name='publisher-rud'),
    path('api01/publishers/', views.PublisherListView.as_view(),
         name='publisher-list-create'),
    path('api01/authors/<int:id>',
         views.AuthorDetailedView.as_view(), name='author-rud'),
    path('api01/authors/', views.AuthorListView.as_view(),
         name='author-list-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
