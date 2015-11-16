#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: cptec_bots.download
    :platform: Unix, Osx, Windows

.. moduleauthor:: Joao Trevizoli Esteves<joao@lab804.com.br>
"""

import os
import shutil
from request_handler import *
from datetime import datetime
from unidecode import unidecode

__author__ = 'joao'


class FileSave(RequestHandler):
    """Image getter and saver

    the class is responsible for dealing
    with cptecs numeric 11 days eta model image. Based
    on the primary key of the image object and which cities
    it represents.

    .. note::
        It's extremely important to use the right city name

    :param: file_name: The file name, preferably the city name.
    :param: file_url: The image url.
    :type: file_name: str
    :type: file_url: str
    """

    base_dir = os.path.abspath(os.path.dirname(__file__)).\
        replace('cptec_bots', '../data')
    base_url = 'http://previsaonumerica.cptec.inpe.br{}'

    def __init__(self, file_name, file_url):
        super(RequestHandler, self).__init__()
        self.file_name = unidecode(file_name.lower())
        self.file_url = file_url

    def __check_folder(self):
        """Check folder existence

        Check if the folder exists, if not
        create it.

        """
        path = os.path.join(self.base_dir, self.file_name)
        if not os.path.exists(path):
            os.makedirs(path)

    def save_file(self):
        """ Save .png file with graph image

        The method downloads the png image file from
        cptec webserver, and saves it to user's computer.
        """
        self.__check_folder()
        n_file_name = u'{}{}.png'.format(self.file_name,
                                         datetime.utcnow().
                                         strftime("_%d_%m_%Y"))
        path = os.path.join(self.base_dir, self.file_name, n_file_name)
        if not os.path.exists(path):
            r = requests.get(self.base_url.format(self.file_url), stream=True)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            else:
                raise CptecException(u'The server returned an wrong'
                                     u'status code of '
                                     u'{}, and it wasn\'t '
                                     u'possible'
                                     u' to continue'.format(r.status_code))
