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
import shutil
from shutil import *
import curses, curses.panel
from  Nexus_Switch import *                                           # Basic switch functions
from  Nexus_Route  import *                                           # Routing Routines
from  RHsocket_lib import *
       

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
	  xrefresh = 80
	  
	  if (xmax > 40): xrefresh = xmax - 2
	                 
	  pad.refresh (0,0,4,1,20, xrefresh)                            # pad.refresh (y,x,from, to,min,max
	  return()



def get_menu(mline=3):
      	#  screen.addstr(4, COL2, "Please enter a number...", hcolor)
	
	menu1 = mline
	COL2  = 17

	hcolor = curses.color_pair(1)
	hmenu1 = curses.A_BOLD
	
	screen.addstr(menu1, COL2,    " Queues   ",hcolor)
        screen.addstr(menu1, COL2+1,   "Q",        hmenu1)
        
	screen.addstr(menu1, COL2+10, " Log file ",hcolor)
        screen.addstr(menu1, COL2+11,  "L",        hmenu1)
        
	screen.addstr(menu1, COL2+20, " Inter.   ",hcolor)
        screen.addstr(menu1, COL2+21, "I", hmenu1)

	screen.addstr(menu1, COL2+30, " Buffer   ",hcolor)
        screen.addstr(menu1, COL2+31,  "B",        hmenu1)

	screen.addstr(menu1, COL2+40, " Routing  ",hcolor)
        screen.addstr(menu1, COL2+41,  "R",        hmenu1)

	screen.addstr(menu1, COL2+50, " EXIT     ",hcolor)
        screen.addstr(menu1, COL2+52,   "X",       hmenu1)

	screen.addstr(menu1, COL2+57, "   ",hcolor)

	smenu1 = "qlibrx"
	screen.refresh()
	
        return (smenu1)

def get_cli_data(cli_string=""):
        
        cli(cli_string, True)
        #  buffer1 = cli_socket_req (cli_string)
        reply = raw_input('Enter to return')
        return()

def get_menu_data (xinput=' '):
      
	if xinput == ord(smenu1[1]):                    # Log file display
		get_Monitor_Status()
		reply = raw_input('Enter to return')
        else:
                curses.endwin()
                
	if xinput == ord(smenu1[3]):  
	        lx_socket_req(-3)                                # Socket --> bufferMonitor
                reply = raw_input('Enter to return')
                
	if xinput == ord(smenu1[0]):  get_cli_data ('show platform software qd info global')	             
	if xinput == ord(smenu1[2]):  get_cli_data ('show int')              # Show interfaces                          
	if xinput == ord(smenu1[4]):  get_cli_data ('sh ip route ospf-1')    # Show ospf           
	if xinput == ord('C'):        get_cli_data ('show system resources') # Show system resources            

        return()

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
        
	COL1 = 8
        COL2 = 40
        mline = 2
	# get_cpu_status()
	
	#buffer_config = get_config_data()                          # Banner, Switch name, Time etc
	#screen.addstr(1, 1, buffer_config,curses.A_REVERSE)  
	title_string = "NexusAccess-0.1                                              "
	
	system_time = get_system_data()
	screen.addstr(1,  1, title_string+system_time,curses.A_REVERSE)

	smenu1 = get_menu(mline)                                   # Menu 

	buffer_mgmt0 = get_mgmt0_ip(mline)                         # Management IP address
        screen.addstr (mline, 1,buffer_mgmt0, hcolor)

	xinput = screen.getch()	
	
	get_menu_data (xinput)	        		

curses.endwin()
