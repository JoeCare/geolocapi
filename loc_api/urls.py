from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('', views.output_loc, name='output-loc'),
	path('loc/', views.input_loc, name='main-loc'),
	]

urlpatterns = format_suffix_patterns(urlpatterns)
