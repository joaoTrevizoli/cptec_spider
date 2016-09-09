#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cptec_crawling.cptec_bots.text_search import PlaceTextFinder
from cptec_crawling.cptec_bots.download import FileSave

__author__ = 'joao'


if __name__ == '__main__':
    _pks = [586, 2467, 4176, 4263]
    for _pk in _pks:
        try:
            print "beginning"
            new_req = PlaceTextFinder(_pk)
            file_obj = FileSave(new_req.find_city(), new_req.find_url())
            file_obj.save_file()
            print "ending"
        except Exception as e:
            print e
