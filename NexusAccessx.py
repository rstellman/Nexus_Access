#!/usr/bin/env python
#
#  NexusAccess_1x .py,pyc
#  Author:  Robert Stellman (rostellm)
#  Date  :  27 Sep 2012 -  New file from NexusAccess.py
#
#  Date  :  27 Nov 2012 -  Incorporating sockets for a remote client
#

import socket
from Nexus_Object import *

import os
from datetime import datetime
import time
import shutil
from shutil import *
import curses, curses.panel


HOSTS=("172.25.187.155","172.25.187.50","172.25.187.155")
HOST = '172.25.187.155'            # The remote host
PORT = 50007                       # The same port as used by the server


Nexus1 = Nexus_switch(HOST,PORT)
      
def stringNexusCLI (sbuffer='',host=HOSTS[0]):
       
    try:     buffer = repr(Nexus1.s_socket(sbuffer,host,PORT))
    except:  return("Socket off-line\n  ....\n")         
         
    return (buffer)

def dsp_output_str(bufferText):
    """ Displays output  \n"""
         
    length = len (bufferText)
    lenx   = length - 1
    
    if (length <= 1):  return()
    
    pad = curses.newpad(100,100)                      # lines, columns
    ymax, xmax = pad.getmaxyx()
    if (ymax >=  30):  ymax =  30
    if (xmax >=  86):  xmax =  86
              
    y=4; x=0 
    
    # '

    n = 0
    while ( n*2500 < length):
         mu = 2500*(n+1)
         ml = 2500*n
         
         pad.clear()
         try: pad.addstr(y,x, bufferText[ml:mu])
         except curses.error: pass      

         # pad.refresh (y,x,ymin,xmin,ymax,xmax)

         try: pad.refresh (0,0,1,1,ymax-2, xmax-2)              
         except curses.error: pass

         n = n + 1
         if ( n*2500 <  length ):  

              title_string = " NexusAccess-0.12m                                                          "
              screen.addstr(1,  1, title_string,curses.A_REVERSE)
              screen.addstr (1, 59 ,host, curses.A_REVERSE)
              smenu1 = get_menu(mline)                                # Menu 
              screen.addstr (3, 1, "Press Enter for more", curses.A_REVERSE)
              screen.refresh()
              screen.move (1,76)
              xinput = screen.getch()   
              if xinput == ord('q'):           
                    screen.addstr (3, 1, "                    ");break

        
         # .... End of loop ........
    
    return()

def get_mgmt0_ip(mline=24,host=HOSTS[0]):
  
    try:     inf1 = stringNexusCLI("show int mgmt0 brief | grep mgmt0", host)
    except:  return ('xx.xx.xx.xx')
          
    o = inf1
    o = Nexus1.stringNexusFormat (o)
      
    o = o.replace ("mgmt0","")
    o = o.replace ("--","")
    o = o.replace ("up","")
    inf = o.lstrip()
    inf1= inf.split(" ")[0]     
    buffer_mgmt0 = "["+inf1+"] "
          
    return(buffer_mgmt0)     
          
def get_script(nexusLogFile = "/bootflash/logs/buffer-nexus.logx"):
    """ Runs the script file on the Nexus Chassis \n"""
      
    bufferText="show host"
      
    try:  buffer1 = open(nexusLogFile,'r')
    except:  return("")
      
    bufferText=buffer1.read()
    buffer1.close()
       
    return(bufferText)

def get_menu(mline=3):
    
    COL2  = 17

    hcolor = curses.color_pair(1)
    hmenu1 = curses.A_BOLD
    
    screen.addstr(mline, 1   , " Script          ",hcolor)
    screen.addstr(mline, 2   , "S",            hmenu1)
    screen.addstr(mline, 9   , "0",            hmenu1)
    screen.addstr(mline, 11  , "1",            hmenu1)
    screen.addstr(mline, 13  , "2",            hmenu1)
    screen.addstr(mline, 15  , "m",            hmenu1)

    screen.addstr(mline, COL2,    " Queues   ",hcolor)
    screen.addstr(mline, COL2+1,   "Q",        hmenu1)
    
    COL2 = COL2+10
    screen.addstr(mline, COL2,    " Log file ",hcolor)
    screen.addstr(mline, COL2+1,   "L",        hmenu1)
    
    COL2 = COL2+10
    screen.addstr(mline, COL2,    " Inter.   ",hcolor)
    screen.addstr(mline, COL2+1,   "I"        ,hmenu1)
    
    COL2 = COL2+10
    screen.addstr(mline, COL2,    " Buffer   ",hcolor)
    screen.addstr(mline, COL2+1,   "B",        hmenu1)

    COL2 = COL2+10
    screen.addstr(mline, COL2,    " Routing  ",hcolor)
    screen.addstr(mline, COL2+1,   "R",        hmenu1)

    COL2 = COL2+10
    screen.addstr(mline, COL2,    " EXIT     ",hcolor)
    screen.addstr(mline, COL2+2,    "X",       hmenu1)
    screen.addstr(mline, COL2+6, "   ",hcolor)

    smenu1 = "qlibrx"
    screen.refresh()
    
    return (smenu1)

def get_cli_data(cli_string="", host ='0', skip=0):

        data = ""
        data = stringNexusCLI(cli_string,host)
        data = Nexus1.stringNexusFormat(data,skip)      
        dsp_output_str(data)
        
        return(data)
        
def get_mcli_data( cli_string="", host ='0'):       

        data = ""
        data = stringNexusCLI(cli_string,host)
        data = Nexus1.stringNexusFormat(data,0)
        data = data.replace  ('"','\n')
        data = data.replace  ("\n   ","")
  
        # dsp_output_str(data)
        
        return(data)

def get_menu_data (xinput=' ', host = HOSTS[0]):
    
    screen.move(2,16) 
    bufferText = ""              
    if xinput == ord(smenu1[0]):  
          get_cli_data ('show platform software qd info global\n', host)
    
    if xinput == ord(smenu1[1]):  # Get Monitor Status
          bufferText = get_script("/root/scripts/srun.txt")                             
          bufferText = Nexus1.stringNexusFormat (bufferText)    
          dsp_output_str(bufferText)
                                  
    if xinput == ord(smenu1[2]):  
          get_cli_data ('show int brief\n',host)
    
    if xinput == ord(smenu1[3]):  
          get_cli_data ('BMdata',host,1) 
    
    if xinput == ord(smenu1[4]):  
          get_cli_data ('sh ip route vrf management\n',host,0)
    
    if xinput == ord('s'):        
          # Run Script
          bufferText = get_script('/root/scripts/script.txt')                             
          bufferm = get_cli_data (bufferText,host,0)
          Nexus1.s_write ("/root/scripts/srun.txt", bufferm)
                                  
    if xinput == ord('0'):
          host    = HOSTS[0] 
          
    if xinput == ord('1'):
          host    = HOSTS[1] 
          
    if xinput == ord('2'):
          host    = HOSTS[2]
    
    if xinput == ord('m'):        
          # Run multi-script
          bufferText = get_script('/root/scripts/mscript.txt')  
                                  
          i = 0; bufferm =""; n = 3
          while (i < n):
                buffer1 = HOSTS[i] + '\n '+ get_mcli_data (bufferText,HOSTS[i]) 
                bufferm = bufferm + buffer1
                i =  i + 1
                                 
                dsp_output_str(bufferm)
                Nexus1.s_write ("/root/scripts/mrun.txt", bufferm)
                                  
    return(host)

# Main
#   .. Create Object
#   .. call getNexusData 
#

os.environ['TERM']='xterm-color'
screen = curses.initscr()

if (curses.has_colors()):
         curses.start_color()
         curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
         hcolor = curses.color_pair(1)
else:
         hcolor = curses.A_NORMAL
                      
xinput = 0
screen.clear()
host = HOSTS[0]

while xinput != ord('x'):
                
    # screen.clear()
    # screen.border(0)
        
    COL1 = 8
    COL2 = 40
    mline = 2

    title_string = " NexusAccess-0.12m                                                          "
    screen.addstr(1,  1, title_string,curses.A_REVERSE)
    screen.addstr (1, 59 ,host, curses.A_REVERSE)
    smenu1 = get_menu(mline)                                # Menu 

    xinput = screen.getch() 
    
    host = get_menu_data (xinput, host)                  

curses.endwin()