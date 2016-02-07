#!/usr/bin/python
import re
import subprocess
import time
import os.path
from uuid import getnode as get_mac

user = "anonymous"
line=subprocess.check_output("speedtest-cli")

getDown = re.search( r'Download: ([0-9]{2}\.[0-9]{2})', line, re.M|re.I)
getUp = re.search( r'Upload: ([0-9]{2}\.[0-9]{2})', line, re.M|re.I)

if getDown:
	dSpeed =  getDown.group(1)
else:
	dSpeed = "No Download!!"

if getUp:
	uSpeed = getUp.group(1)
else:
	uSpeed = "No Upload!!"

date = time.strftime("%d/%m/%Y")
hour = time.strftime("%H:%M:%S")
time = time.strftime("%H:%M:%S")

print "Date + Time: " + date + " " + hour
print "Download Speed:" + dSpeed
print "Upload Speed:" + uSpeed

mac = get_mac()

## write in file

filelog = 'speedlog.csv'
exists = os.path.isfile(filelog)
fd = open(filelog,'a')

if not exists:
 fd.write("Date, Hour, dSpeed, USpeed, MAC, User")

fd.write('\n' + date + "," + hour + "," + dSpeed + "," + uSpeed + "," + str(mac) + "," + user)
fd.close()


## Sources:
# blog: http://www.raspberrypi-spy.co.uk/2015/03/measuring-internet-speed-in-python-using-speedtest-cli/
# downlaod zip: https://github.com/sivel/speedtest-cli.git
