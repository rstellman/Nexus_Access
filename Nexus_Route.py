#!/usr/bin/env python
#
#  Nexus_Route.py,pyc
#  Author:  Robert Stellman (rostellm)
#  Date  :  17 Jul 2012 -  Initial File Created


import cisco 
from cisco import *
import Nexus_Route                                              # Routing Routines


def show_mac_table():
        cli('show mac address-table dynamic', True)
        return

def get_routing():
        cli('show routing',True)
        return()

