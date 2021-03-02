from rest_framework.utils import json
from rest_framework_jsonp import renderers
from rest_framework_jsonp.renderers import JSONPRenderer
from json import JSONEncoder as jJCODER


class FromDict(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)


def dict2cls(d):
    return json.loads(json.dumps(d), object_hook=FromDict)
