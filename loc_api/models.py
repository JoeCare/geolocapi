from rest_framework import documentation
from rest_framework import request, relations, response
from rest_framework import versioning
from rest_framework_jsonp import renderers

from django.db import models

# class DataLoader(models.Model):
#     CHOICES = []
#     performed = models.DateTimeField(auto_now_add=True)
#     input_ipv4 = models.GenericIPAddressField(default='check', help_text='')
#     user_input = models.IntegerChoices()


class Geolocator(models.Model):

    # ordered_by = models.ForeignKey('auth.User', related_name='locations',
    #                           on_delete=models.CASCADE)
    performed = models.DateTimeField(auto_now_add=True)
    input_ipv4 = models.GenericIPAddressField(default='check',
                                              help_text='or:')
    # input_ip = models.GenericIPAddressField(default='check',
    #                                           help_text='ipv4, ipv6')
    input_domain = models.URLField(blank=True)
    collected_data = models.TextField(help_text='Appended geolocalization '
                                                'data', editable=False,
                                      null=True)
    geolocation_base = models.URLField(default='http://api.ipstack.com/')
    input_domain = models.URLField(blank=True, help_text='')

    def __str__(self):
        return self.id

    """
    i teraz kwestia czy jak typo postuje te dane to
     moze niech one sie tu zapisza oprocz colleted_data - to by bylo jako 
     Foreign z z modelu np. LocationsData gdzie by sie jakos wywolywal 
     endpoint do ipshack
     """
