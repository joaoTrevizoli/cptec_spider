#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. module:: cptec_bots.request_handler
    :platform: Unix, Osx, Windows

.. moduleauthor:: Joao Trevizoli Esteves<joao@lab804.com.br>
"""


import requests

__author__ = 'joao'


class CptecException(Exception):
    """Cptec webserver Exceptions

    Raises exceptions when cptec web server
    returns an status code different from 200

    :raises: CptecException
    """
    pass


class RequestHandler(object):
    """Handles requests

        This class is the base class for connecting
        with cptecs webserver, all the requests classes
        are based here.

        :param: pk: Primary key
        :type: pk: int
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
        """Response data object

        This setter sets data to the response object
        from the get method from server. it uses the
        primary key to build the url for the request.

        Sets:

            data: server object response.
        """
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

