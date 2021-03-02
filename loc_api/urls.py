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
from django.conf.urls import include, re_path
from faker.providers import company
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet


router = DefaultRouter()
router.register(company, CompanyViewSet, base_name='company')

urlpatterns = [
    re_path('^', include(router.urls)),
]
