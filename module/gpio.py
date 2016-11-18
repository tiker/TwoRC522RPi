#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Class in Python 2.7 for incorporation of the RPi.GPIO module to control the GPIO channels of Raspberry Pi.

Credits and License: Created by Erivando Sena (2016)

 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License.
"""

import RPi.GPIO as GPIO

__author__ = "Erivando Sena Ramos"
__copyright__ = "Erivando Sena (2016)"
__email__ = "erivandoramos@bol.com.br"
__status__ = "Prototype"


class PinosGPIO(object):
    
    gpio = None

    def __init__(self):
        self.gpio = GPIO
        