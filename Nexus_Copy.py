#  Copy file from rostellm directory to flash drive
#
#  04 May 2012 - R. Stellman: Basic
#

import cisco 
from cisco import *


protocol="scp"
host    = "172.25.187.45"
source  = "bootflash:///logs/buffer-nexus.logx.py"
dest    = "~daystrom/scripts/buffer-nexus.logx.py"
user    = "daystrom"
password = "test"
login_timeout=10
vrf="management"

# CLI - copy scp://rostellm@10.10.1.22/home/rostellm/scripts/Nexus_Copy.py bootflash:///scripts/Nexus_Copy.py


# def transfer (protocol = "", host = "", source = "", dest = "", vrf = "management", login_timeout=10, user = "", password = ""):

#

c = transfer ("scp",host,source, dest, vrf, 10, user, password)

pinrt ("c = "+ c)
print ("Done")
