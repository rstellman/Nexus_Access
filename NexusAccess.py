#!/usr/bin/env python
#
#  NexusAccess .py,pyc
#  Author:  Robert Stellman (rostellm)
#  Date  :  20 Mar 2012
#
#  Date  :  03 May 2012 -  Structure defined
#  Date  :  23 Jun 2012 -  Cleaned up code
#  Date  :  26 Jun 2012 -  Added MAC Table function

import cisco 
from cisco import *
import os
from datetime import datetime
import time
import string
import shutil
from shutil import *
import curses, curses.panel
from  RHsocket_lib import *

class nexus(object):

    def getNexusBasic(self):
        """\n \t Responds to Request for Data\n"""
          
    def getNexusBGP(self):
        """\n \t Responds to Request for Data\n"""
 

# show_system
def cpu_status():   
           """ \n
           System resources are displayed CPU load etc.
           \n"""
           cli('show system resources', True)
           return ()

# show global queues

def show_queues():
          cli('show platform software qd info global',True)
          return()

# Show interface eg. mgmt, eth1/1 etc

def show_run():
          cli('show int', True)
          return()

def show_mac_table():
          cli('show mac address-table dynamic', True)
          return


def get_Monitor_Status():
          """ System resources are displayed CPU load etc.\n"""
          #  nexusLogFile = "/bootflash/logs/buffer-nexus.logx":
          """ System resources are displayed CPU load etc.\n"""
          nexusLogFile = "/bootflash/logs/buffer-nexus.logx"
          bufferText=" ... "
          buffer1 = open(nexusLogFile,'r')
          bufferText=buffer1.read()
          buffer1.close()
          bufferText = bufferText.replace  ("(0, '","")
	  bufferText = bufferText.replace  ("')","")
	  bufferText = bufferText.replace  ("-","")
	  bufferText = bufferText.replace  ("|","")
	  bufferText = bufferText.replace  ("\\n","\n\r")
	  
	  pad = curses.newpad(20,120)                              # 20 lines, 120 columns
	          
	  y=3; x=0   
	  try: pad.addstr(y,x, bufferText)
	  except curses.error: pass	
	  
	  ymax, xmax = pad.getmaxyx()
	  if (xmax > 40):
	                 xrefresh = xmax - 2
	  else:
	                 xrefresh = 80
	                 
	  pad.refresh (0,0,4,1,20, xrefresh)                            # pad.refresh (y,x,from, to,min,max
	  return()
          
                 
def get_cpu_load(self):
          # get cpu load status
          return()

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
        
        hstring = maxCell+Remaining+ Switch_cnt+Total_Usage+"   "
        screen.addstr(hline,  1, " Max cell/remain/switch/total= "+hstring  , hcolor )
        return()
     
def get_config_data():

        hconfig = curses.A_REVERSE
        
        COL1= 1
        s,o = cli("show hostname")
        o = repr(o)
        o = o.replace  ("\\n","")
        o = o.replace  ("'","")
        host=o

        s,o = cli("show banner motd")
        o = repr(o)
        o = o.replace  ("\\n","")        
        o = o.replace  ("'","")
        banner=o
    
        s,o = cli("show clock")
        o = repr(o)
        o = o.replace  ("\\n","")
        o = o.replace  ("'","")
        clock=o
        
        screen.addstr(1, COL1, " "+banner+" > "+host+"              "+clock+"   ", hconfig)  
        
        return()
     

def get_routing():
        cli('show routing',True)
        return()

def get_ospf_status():
        cli('sh ip route ospf-1', True)
        return()
        
def get_mgmt0_ip(mline=24):
        s, inf1 = cli("show int mgmt0 brief | grep mgmt0")
        o = inf1
        hcolor = curses.color_pair(1)
        o = o.replace ("mgmt0","")
        o = o.replace ("--","")
        o = o.replace ("up","")
        inf = o.lstrip()
        inf1= inf.split(" ")[0]     
        screen.addstr (mline, 1,"["+inf1+"] ", hcolor)
        
        return()     
        
def get_menu(mline=3):
      	#  screen.addstr(4, COL2, "Please enter a number...", hcolor)
	
	menu1 = mline
	COL2  = 17

	hcolor = curses.color_pair(1)
	screen.addstr(menu1, COL2,    " Queues   ",hcolor)
	screen.addstr(menu1, COL2+10, " Log file ",hcolor)
	screen.addstr(menu1, COL2+20, " Inter.   ",hcolor)
	screen.addstr(menu1, COL2+30, " Buffer   ",hcolor)
	screen.addstr(menu1, COL2+40, " OSPF     ",hcolor)
	screen.addstr(menu1, COL2+50, " EXIT     ",hcolor)
	screen.addstr(menu1, COL2+57, "   ",hcolor)

        hmenu1 = curses.A_BOLD
	screen.addstr(menu1, COL2+1,  "Q", hmenu1)
	screen.addstr(menu1, COL2+11, "L", hmenu1)
	screen.addstr(menu1, COL2+21, "I", hmenu1)
	screen.addstr(menu1, COL2+31, "B", hmenu1)
	screen.addstr(menu1, COL2+41, "O", hmenu1)
	screen.addstr(menu1, COL2+52, "X", hmenu1)
	smenu1 = "qlibox"
	screen.refresh()
        return (smenu1)
  
# Main
#   .. Create Object
#   .. call getNexusData 
#

NX = nexus()

os.environ['TERM']='xterm-color'
screen = curses.initscr()

if (curses.has_colors()):
         curses.start_color()
         curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
         hcolor = curses.color_pair(1)
else:
         hcolor = curses.A_REVERSE
                      


xinput = 0

while xinput != ord('x'):
              
        screen.clear()
        # screen.border(0)
        
	# xp = string.upper(repr(xinput))	
        # hmenu1 = curses.A_BOLD
	# screen.addstr(5, 20,  "xinput ="+xp, hmenu1)

	COL1 = 8
        COL2 = 40
        
	# Column 1 data
	
	# get_cpu_status()
	
	get_config_data()
	smenu1 = get_menu(2)                                   # Menu 
	get_mgmt0_ip(2)

	xinput = screen.getch()	
	
	
	if xinput == ord(smenu1[0]):
		curses.endwin()
		show_queues()
		reply = raw_input('Enter to return')

	if xinput == ord(smenu1[1]):
		#curses.endwin()
		get_Monitor_Status()
		reply = raw_input('Enter to return')
		
	if xinput == ord(smenu1[2]):
	        curses.endwin()
	        show_run()
	        reply = raw_input('Enter to return')
	        
	if xinput == ord(smenu1[3]):
	        curses.endwin()
	        lx_socket_req("5")
	        reply = raw_input('Enter to return')
	               
	if xinput == ord(smenu1[4]):
	        curses.endwin()
	        get_ospf_status()
	        reply = raw_input('Enter to return')	        

	if xinput == ord('c'):
		curses.endwin()
		get_cpu_status(4)
		reply = raw_input('Enter to return')
	        		

curses.endwin()
