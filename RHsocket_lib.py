#
# Name                  Samuel Kommu, Robert Stellman
# Modified from         Jacob Rapp's SocketClient.py
# Modified              To run on more versions of Python by R. Stellman
#                       And added help section

"""\n  bufferClient \n      
   \t  ... Works with bufferMonitorThread.py
   \t  ... Use:  python bufferClient.py  n
   \t  ...       where n is the number of lines of data you want
   \t  ... Note: This program runs once and then ends.
   \t  ...       Developed on Python 2.7.2
   \t ..
   \n """

import sys
from socket import *                                      # get socket constructor and constants


def lx_socket_req (message ="10"):

     serverHost = "172.25.187.155"
     serverPort =  50007                                  # non-reserved port used by the server
 
     #message = "10"                                      # default text to send to server
                                                          # requires bytes: b'' or str,encode()                                            
     error = 0   
     sockobj = socket(AF_INET, SOCK_STREAM)               # make a TCP/IP socket object

     try:
             sockobj.connect((serverHost, serverPort))    # connect to server machine + port
     except:
             error = 1
             
     if (error == 0):
             sockobj.send(message)                        # send line to server over socket
             data = sockobj.recv(10800)                   # receive line from server

             for value in data.split(' '):
                            print (value)
                    
             sockobj.close()                              # close socket to send eof to server
             
     else:
             print(".. Socket Server not active " )
             
     return()
     
     
# use - lx_socket_req("5")   

 
                                
