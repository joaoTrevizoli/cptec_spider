#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'joao'

from cptec_crawling.cptec_bots.text_search import PlaceTextFinder
from cptec_crawling.cptec_bots.download import FileSave
from cptec_crawling.image_analyser.img_analyser import GraphInterpreter

if __name__ == '__main__':
    _pks = [586, 2467, 4176, 4263]
    for _pk in _pks:
        try:
            print "comecando"
            new_req = PlaceTextFinder(_pk)
            file_obj = FileSave(new_req.find_city(), new_req.find_url())
            file_obj.save_file()
            print "terminado"
        except Exception as e:
            print e

    humidity_arara = GraphInterpreter('araraquara/araraquara_11_11_2015.png',
                                (0, 10),
                                'rain')

    print type(humidity_arara.np_image_matrix())
    humidity_arara.save_values()