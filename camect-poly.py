#!/usr/bin/env python
# 
from udi_interface import Interface,LOGGER
import sys

""" Grab My Controller Node """
from nodes import CamectController,VERSION

if __name__ == "__main__":
    try:
        polyglot = Interface([])
        polyglot.start(VERSION)
        polyglot.updateProfile()
        polyglot.setCustomParamsDoc()
        CamectController(polyglot, 'controller', 'controller', 'Camect Controller')
        polyglot.runForever()
    except (KeyboardInterrupt, SystemExit):
        LOGGER.warning("Received interrupt or exit...")
        polyglot.stop()
    except Exception as err:
        LOGGER.error('Excption: {0}'.format(err), exc_info=True)
    sys.exit(0)
