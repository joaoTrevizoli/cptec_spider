#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. module:: cptec_bots.text_search
    :platform: Unix, Osx, Windows

.. moduleauthor:: Joao Trevizoli Esteves<joao@lab804.com.br>
"""
__author__ = 'joao'


import re

from . import RequestHandler


class CityNameException(Exception):
    """CityName Exception

    Raises when a city isn't found

    :raises: CityName Exception
    """
    pass


class PlaceTextFinder(RequestHandler):

    def find_city(self):
        """ Look for cities in text

        Try to find cities inside the html text
        using regular expression

        :returns: City name
        :rtype: str
        """
        try:
            city = re.search(ur'0{2}Z - ([\w+\s]+)', self.data.text, re.UNICODE).group(1)
            return city
        except:
            raise CityNameException(u"The regex wasn't capable to"
                                    u"return the city name")

    def find_url(self):
        """Find image urls

        Search for image urls inside the html text
        using regular expression

        :returns: Url
        :rtype: str
        """
        i_url = '/golMapWeb/image-cache'
        e_url = re.search(ur'(/\w+[.]png)', self.data.text).group(1)
        return '{}{}'.format(i_url, e_url)