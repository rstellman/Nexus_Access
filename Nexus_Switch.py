#!/usr/bin/env python
#
#  Nexus_Switch.py,pyc
#  Author:  Robert Stellman (rostellm)
#  Date  :  17 Jul 2012 -  Initial File Created
#

import cisco 
from cisco import *
import os
from datetime import datetime
import time
import shutil
from shutil import *
import curses, curses.panel




class nexus(object):

    def getNexusBasic(self):
        """\n \t Responds to Request for Data\n"""
          
    def getNexusBGP(self):
        """\n \t Responds to Request for Data\n"""

                
def execute_cmd(cmd_string):
	
	system("clear")
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Command executed correctly"
	else:
		print "Command terminated with error"
	raw_input("Press enter")
	print ""
	return()

def get_cpu_status(hline=4):
        
        b1=BufferDepthMonitor()
        maxCell     =  " "+repr(b1.get_max_cell_usage())
        Remaining   =  ", "+repr(b1.get_remaining_instant_usage())
        Switch_cnt  =  ", "+repr(b1.get_switch_cell_count())
        Total_Usage =  ", "+repr(b1.get_total_instant_usage())
        
        hcolor = curses.color_pair(1)
        
        hstring = " Max cell/remain/switch/total= "+maxCell+Remaining+ Switch_cnt+Total_Usage+"   "
        return(hstring)
     
def clear_format (cli_string =" "):

        s,fstring = cli(cli_string)
        fstring = repr(fstring)
	fstring = fstring.replace  ("\\n","")
	fstring = fstring.replace  ("'","")
	return (fstring)
	
      
def get_config_data():

        host   = clear_format("show hostname")
        banner = clear_format("show banner motd")
        clock  = clear_format("show clock")
        Weekday= clock.split(" ")[2]
        Month  = clock.split(" ")[3]
        Day    = clock.split(" ")[4]
        Year   = clock.split(" ")[5]
        Date   = Weekday+" "+Day+" "+Month+" "+Year
        
        buffer_config = " "+banner+" > "+host+"                               "+Date+"   "
        
        return(buffer_config)

def get_system_data():

        clock  = clear_format("show clock")
	Weekday= clock.split(" ")[2]
	Month  = clock.split(" ")[3]
	Day    = clock.split(" ")[4]
	Year   = clock.split(" ")[5]
	Date   = Weekday+" "+Day+" "+Month+" "+Year
	
	return(Date)


def get_mgmt0_ip(mline=24):

        s, inf1 = cli("show int mgmt0 brief | grep mgmt0")
        o = inf1
        o = o.replace ("mgmt0","")
        o = o.replace ("--","")
        o = o.replace ("up","")
        inf = o.lstrip()
        inf1= inf.split(" ")[0]     
        buffer_mgmt0 = "["+inf1+"] "
        
        return(buffer_mgmt0)     
        
