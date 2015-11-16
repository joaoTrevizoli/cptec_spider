#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cptec_crawling.image_analyser.img_analyser import GraphInterpreter


__author__ = 'joao'


if __name__ == '__main__':

    # Araraquara
    araraquara = GraphInterpreter('araraquara/araraquara_13_11_2015.png',
                                (0, 10),
                                'rain')

    araraquara.save_values()

    araraquara = GraphInterpreter('araraquara/araraquara_13_11_2015.png',
                                (18, 35),
                                'temp')

    araraquara.save_values()

    araraquara = GraphInterpreter('araraquara/araraquara_13_11_2015.png',
                                (30, 100),
                                'humidity')

    araraquara.save_values()

    ############################ Fim #####################################


    # Iracemapolis

    iracemapolis = GraphInterpreter('iracemapolis/iracemapolis_13_11_2015.png',
                                (0, 10),
                                'rain')

    iracemapolis.save_values()

    iracemapolis = GraphInterpreter('iracemapolis/iracemapolis_13_11_2015.png',
                                (16, 37),
                                'temp')

    iracemapolis.save_values()

    iracemapolis = GraphInterpreter('iracemapolis/iracemapolis_13_11_2015.png',
                                (30, 100),
                                'humidity')

    iracemapolis.save_values()

    ############################ Fim #####################################

    # Pradopolis

    pradopolis = GraphInterpreter('pradopolis/pradopolis_13_11_2015.png',
                                (0, 10),
                                'rain')

    pradopolis.save_values()

    pradopolis = GraphInterpreter('pradopolis/pradopolis_13_11_2015.png',
                                (19, 35),
                                'temp')

    pradopolis.save_values()

    pradopolis = GraphInterpreter('pradopolis/pradopolis_13_11_2015.png',
                                (40, 100),
                                'humidity')

    pradopolis.save_values()

    ############################ Fim #####################################

    # Quirinopolis

    quirinopolis = GraphInterpreter('quirinopolis/quirinopolis_13_11_2015.png',
                                (0, 10),
                                'rain')

    quirinopolis.save_values()

    quirinopolis = GraphInterpreter('quirinopolis/quirinopolis_13_11_2015.png',
                                (19, 34),
                                'temp')

    quirinopolis.save_values()

    quirinopolis = GraphInterpreter('quirinopolis/quirinopolis_13_11_2015.png',
                                (40, 100),
                                'humidity')

    quirinopolis.save_values()