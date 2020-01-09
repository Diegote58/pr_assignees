#!/usr/bin/python

from collections import namedtuple
import requests
import random
import json
import sys

ACCESS_TOKEN = '26a37d7365053f983200b18fa09a10964f343f7d'
PROJECT = 'fury_withdraw-gaas-consumer'
OWNER = 'mercadolibre'

class RestClient():
    
    def get(self, uri, headers = None, base = None, access_token = None):

        if not base:
            base = BASE

        if uri.find('?') >= 0:
            accessTokenParam = "&access_token=%s" % (access_token)
        else:
            accessTokenParam = "?access_token=%s" % (access_token)

        uri = "https://%s/%s%s" % (base, uri, accessTokenParam)

        print("uri: %s" % (uri))

        jsonObj = requests.get(uri, headers=headers)

        #print(jsonObj.text)

        obj = json.loads(self.filterResponse(jsonObj.text), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        return obj

    def post(self, uri, headers = {}):
        jsonObj = requests.post("http://%s" % (uri), headers=headers)
        obj = json.loads(jsonObj.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        return obj

    def filterResponse(self, data):
        filters = [
                    {
                        'value': '_links',
                        'replace': 'links'
                    }
                ]

        for element in filters:
            output = data.replace(element['value'], element['replace'])

        return output
