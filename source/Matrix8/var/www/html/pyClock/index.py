#!/usr/bin/python3

import cgi, cgitb, configparser
form = cgi.FieldStorage()
config = configparser.ConfigParser()

# ini file
config.read('/var/lib/pyClock/pyClock.ini')
clockconfig = config['CLOCK']
# __DEBUG__
#print (clockconfig['Display'])
#print (clockconfig['TimeZone'])
#print (clockconfig['Hour1'])
#print (clockconfig['Brightness1'])
#print (clockconfig['Hour2'])
#print (clockconfig['Brightness2'])

print("Content-Type: text/html")
print (
"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width" />
<link rel='stylesheet' id='dark-css'  href="./style.css" type="text/css" media="all" />
<title>Clock Control</title>
</head>
<body>
<H2>Clock Control</H2>

<P>Snake languages are at work here</P>
"""
)
# __DEBUG__
#print("<P>Values from .ini file")
#print("Display: ", clockconfig['Display'])
#print("TimeZone: ", clockconfig['TimeZone'])
#print("Hour1: ",clockconfig['Hour1'])
#print("Brightness1", clockconfig['Brightness1'])
#print("Hour2: ",clockconfig['Hour2'])
#print("Brightness2", clockconfig['Brightness2'])
#print("</P>")
print (
"""

<form action="/pyClock/submit.py" method="post">
This clock runs in <select name="TimeZone">
"""
)
tlist = ['HST', 'US/Alaska', 'PST8PDT', 'MST', 'MST7MDT', 'CST6CDT', 'EST5EDT', 'UTC']
for t in tlist:
  if t == clockconfig['TimeZone']:
    print("<option value=\"",t,"\" selected>",t,"</option>",sep="")
  else:
    print("<option value=\"",t,"\">",t,"</option>",sep="")
print (
"""
</select> timezone (the zone names with *DT and Alaska observe DST)
<br>
Set brightness of display to value
<select name="Brightness1">
"""
)
blist = ['0', '1', '2', '4', '8', '16', '32', '64', '128', '192', '224', '255']
for b in blist:
  if b == clockconfig['Brightness1']:
    print("<option value=\"",b,"\" selected>",b,"</option>",sep="")
  else:
    print("<option value=\"",b,"\">",b,"</option>",sep="")
print (
"""
</select>
at
<select name="Hour1">
"""
)
for h in list(range(24)):
  if h == int(clockconfig['Hour1']):
    print("<option value=\"",h,"\" selected>",format(h, '02d'),":00</option>",sep="")
  else:
    print("<option value=\"",h,"\">",format(h, '02d'),":00</option>",sep="")
print (
"""
</select>
 hours.
<br>
Set brightness of display to value
<select name="Brightness2">
"""
)
blist = ['0', '1', '2', '4', '8', '16', '32', '64', '128', '192', '224', '255']
for b in blist:
  if b == clockconfig['Brightness2']:
    print("<option value=\"",b,"\" selected>",b,"</option>",sep="")
  else:
    print("<option value=\"",b,"\">",b,"</option>",sep="")
print (
"""
</select>
at
<select name="Hour2">
"""
)
for h in list(range(24)):
  if h == int(clockconfig['Hour2']):
    print("<option value=\"",h,"\" selected>",format(h, '02d'),":00</option>",sep="")
  else:
    print("<option value=\"",h,"\">",format(h, '02d'),":00</option>",sep="")
print (
"""
</select>
 hours.
<br>
<A HREF="./help.html">Help</A>
<br>
<input type="submit" style="background-color:green" value="Submit"/>
"""
)
print ("<input type=\"hidden\" name=\"oldTz\" value=\"",clockconfig['TimeZone'],"\"/>",sep="")
print (
"""
</form>

</body>
</html>
"""
)
