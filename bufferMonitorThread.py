"""\n bufferMonitorThread \n
\t ... Works with bufferClient.py
\t ... Use: python bufferMonitorThread
\t ... Input:  number of lines to output;  
\t             -2 to close thread
\t             -1 to write to file
\t              0 to send out all values
\t
\t ... Note: This program runs continously until you disconnect
\t ... Developed on Python 2.7.2
\t ..
\n """

from cisco import *
from datetime import datetime
import time
from socket import *
from sys import *
from string import join


# Get server IP
# 28 Jun 2012    -  Robert Stellman

s, inf1 = cli("show int mgmt0 brief | grep mgmt0");  o = inf1       
o = o.replace ("mgmt0",""); o = o.replace ("--",""); o = o.replace ("up",""); inf = o.lstrip()

myHost = inf.split(" ")[0]                  # server name, or IP

#............ End of serverHost section


myPort = 50007                  # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)          # make a TCP socket object
sockobj.bind((myHost, myPort))                  # bind it to server port number
sockobj.listen(3)                               # listen, allow 5 pending connects
sockobj.settimeout(1)

bufferValues = []
oCli = CLI('show hardware internal buffer info pkt-stats brief', False)

counter=0
while True:                                             # listen until process killed
        connectionFailed = False
        curDate=datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        oCli.rerun()
        f, m, bUsage = oCli.get_raw_output().split("\n")[4].rpartition(' ')
        bufferValues.append(curDate + "," + bUsage)
        time.sleep(1)
        
        try:
                connection, address = sockobj.accept()         # Check for any connection requests
        except :    
                connectionFailed = True                        # In case of no connection requests - 
                pass
        if ( connectionFailed != True ):
                data = int(connection.recv(10800))             # read next line on client socket
                bvCount=len(bufferValues)
                
                if ( data < bvCount ):                         # Check that request is within range
                        # Done with the monitoring - close the main thread
                        if ( data == -3 ):
                             connection.send(" -3 received")
                        if ( data == -2 ):
                                break;
                        # Save to file ...
                        if ( data == -1 ):
                                bufferFileName = "/bootflash/buffer.inmem.txt"
                                bufferFile = open(bufferFileName, 'w')
                                for Value in bufferValues:
                                        bufferFile.write("%s\n" % Value)
                                bufferFile.close()
                        # Send out all the values
                        elif ( data == 0 ):
                                connection.send(join(bufferValues))
                        # Send out a range of values - last x units
                        else:
                                connection.send(join(bufferValues[(bvCount-data):bvCount]))
                else:
                        connection.send("Invalid index")
                connection.close()
