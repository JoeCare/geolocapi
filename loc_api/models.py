import requests, os
from rest_framework import documentation
from rest_framework import request, relations, response
from rest_framework import versioning
from rest_framework_jsonp import renderers
from rest_framework_jwt import authentication
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    street_line_1 = models.CharField(max_length=255)
    street_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']


class Geolocator(models.Model):

    ip_sample = '134.291.210.155'
    sample_url = requests.get(
        f"http://api.ipstack.com/{ip_sample}?access_key="
        f"{os.getenv('ipstackKey')}"
        f"&security=1&hostname=1").json()

    performed = models.DateTimeField(auto_now_add=True)
    input_ipv4 = models.GenericIPAddressField(default='check', help_text='or:')
    input_domain = models.URLField(blank=True)

    def __str__(self):
        return self.__class__()
