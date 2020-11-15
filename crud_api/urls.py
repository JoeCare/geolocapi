from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('auth/', include('rest_framework.urls')),
    path('books/<int:id>', views.BookDetailedView.as_view(), name='book-rud'),
    path('books/', views.BookListView.as_view(), name='book-list-create'),
    path('publishers/<int:id>',
         views.PublisherDetailedView.as_view(), name='publisher-rud'),
    path('publishers/', views.PublisherListView.as_view(),
         name='publisher-list-create'),
    path('authors/<int:id>', views.AuthorDetailedView.as_view(), name='author-rud'),
    path('authors/', views.AuthorListView.as_view(), name='author-list-create'),
    # path(r'^(?P<pk=id>\d+)/$', BookRudView.as_view(), name='post-rud'),
    # path(r'^(?P<pk>\d+)/$', BookRudView.as_view(), name='post-rud'),  # -oryginal
]
