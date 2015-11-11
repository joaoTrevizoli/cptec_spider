#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'joao'

import os
import shutil
from request_handler import *
from datetime import datetime


class FileSave(RequestHandler):
    """
    Creates folder and saves files
    """

    base_dir = os.path.abspath(os.path.dirname(__file__)).replace('cptec_bots', 'data')
    base_url = 'http://previsaonumerica.cptec.inpe.br{}'

    def __init__(self, file_name, file_url):
        super(RequestHandler, self).__init__()
        self.file_name = file_name.lower()
        self.file_url = file_url

    def __check_folder(self):
        path = os.path.join(self.base_dir, self.file_name)
        if not os.path.exists(path):
            os.makedirs(path)

    def save_file(self):
        self.__check_folder()
        n_file_name = u'{}{}.png'.format(self.file_name, datetime.utcnow().strftime("_%d_%m_%Y"))
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
                                     u'possible to continue'.format(r.status_code))