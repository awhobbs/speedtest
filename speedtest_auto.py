#!/usr/bin/python
import re
import subprocess
import time

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

time = time.strftime("%d/%m/%Y:%H:%M:%S")

print "Date + Time:" + time
print "Download Speed:" + dSpeed
print "Upload Speed:" + uSpeed

fd = open('speedlog.csv','a')
fd.write('\n' + time + "," + dSpeed + "," + uSpeed)
fd.close()



## Sources:
# blog: http://www.raspberrypi-spy.co.uk/2015/03/measuring-internet-speed-in-python-using-speedtest-cli/
# downlaod zip: https://github.com/sivel/speedtest-cli.git