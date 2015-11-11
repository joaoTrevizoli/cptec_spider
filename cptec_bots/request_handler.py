#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'joao'

import requests
import re

class CptecException(Exception):
    pass


class RequestHandler(object):
    """
    Handles requests from cptec servers
    """

    base_url = 'http://previsaonumerica.cptec.inpe.br/golMapWeb/ProcessMeteoId?id={}&modelo=Eta15P'

    def __init__(self, pk):
        self.pk = pk
        self.data = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
        try:
            data_request = requests.get(self.base_url.format(self.pk))
            if data_request.status_code == 200:
                self.__data = data_request
            else:
                raise CptecException(u'The server returned an wrong'
                                     u'status code: {}'.format(data.status_code))

        except:
            raise CptecException(u'The cptec server returned'
                               u' an error please call joao ')

