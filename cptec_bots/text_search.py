#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'joao'

from request_handler import *


class CityNameException(Exception):
    pass


class PlaceTextFinder(RequestHandler):

    def find_city(self):
        try:
            city = re.search(ur'0{2}Z - ([\w+\s]+)', self.data.text, re.UNICODE).group(1)
            return city
        except:
            raise CityNameException(u"The regex wasn't capable to"
                                    u"return the city name")

    def find_url(self):
        i_url = '/golMapWeb/image-cache'
        e_url = re.search(ur'(/\w+[.]png)', self.data.text).group(1)
        return '{}{}'.format(i_url, e_url)