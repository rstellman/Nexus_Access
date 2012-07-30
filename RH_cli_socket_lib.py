#
# Name                  Samuel Kommu, Robert Stellman
# Modified from         Jacob Rapp's SocketClient.py
# Modified              To run on more versions of Python by R. Stellman
#                       And added help section

"""\n  RH_cli_socket_lib \n      
   \t  ... Works with Cli_Monitor_Thread.py
   \t  ... Use:  python bufferClient.py  n
   \t  ...       where n is the number of lines of data you want
   \t  ... Note: This program runs once and then ends.
   \t  ...       Developed on Python 2.7.2
   \t ..
   \n """

import sys
from socket import *                                      # get socket constructor and constants
import time

def cli_socket_req (message =""):

     serverHost = "172.25.187.155"
     serverPort =  50007                               # non-reserved port used by the server
     ncount  = 1
     message = "[b'1']"                               # default text to send to server
                                                      # requires bytes: b'' or str,encode()
     message = (x.encode() for x in ncount)
     # Debug message
     # message ="show int brief"
     
     sockobj = socket(AF_INET, SOCK_STREAM)            # make a TCP/IP socket object
     sockobj.connect((serverHost, serverPort))         # connect to server machine + port

     #for line in message:
     sockobj.send(message)                         # send line to server over socket
     data = sockobj.recv(10800)                    # receive line from server

     for value in data.split(' '):
         print (value)
                    
     sockobj.close()                               # close socket to send eof to server
                
     else:
       
              print ("Use:  python bufferClient.py  n")
       
     return()
     
 
     
     
# use - lx_socket_req("5")   

 
                                
