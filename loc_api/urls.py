# from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
#
# urlpatterns = [
# 	path('', views.output_loc, name='output-loc'),
# 	path('loc/', views.input_loc, name='main-loc'),
# 	]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from django.conf.urls import include, re_path
from faker.providers import company
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, OutputGeoSerializer, input_loc, \
    LocationsModelViewSet, LocationsViewSet, UserViewSet


router = DefaultRouter()
router.register(r'locset', LocationsViewSet, basename='simvs')
router.register(r'locsetm', LocationsModelViewSet)
router.register(f'users', UserViewSet)
# router.register(company, CompanyViewSet, basename='company')

urlpatterns = [
    path('com/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='comp'),
    path('', input_loc, name='in-loc')
]

urlpatterns += router.urls
