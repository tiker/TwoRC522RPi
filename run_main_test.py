#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Class in Python 2.7 for testing two RFID readers with Raspberry Pi.

Use: 
$ cd TwoRC522RPi/
$ sudo python run_main_test.py 
Press Ctrl + C to finish.

Credits and License: Created by Erivando Sena (2016)

 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License.
"""

import sys
from module.leitor_cartao import LeitorCartao

__author__ = "Erivando Sena Ramos"
__copyright__ = "Erivando Sena (2016)"
__email__ = "erivandoramos@bol.com.br"
__status__ = "Prototype"


def main(self):
    
    reader_card = LeitorCartao()
    try:
        while True:
            if not reader_card.isAlive():
                reader_card.start()
    except KeyboardInterrupt:
        print "trl+C received! Sending kill to " + reader_card.getName()
        if reader_card.isAlive():
            reader_card._stopevent.set()
            
if __name__ == '__main__':
    main(sys.argv)
  
    