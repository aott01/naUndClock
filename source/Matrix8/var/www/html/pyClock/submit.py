#!/usr/bin/python3

import os, signal
import cgi, cgitb, configparser
form = cgi.FieldStorage()
config = configparser.ConfigParser()

error = 0

if form.getvalue('oldTz'):
  myOldTz = form.getvalue('oldTz')
else:
  myOldTz = "oldTz undefined"
  error += 1
if form.getvalue('TimeZone'):
  myTz = form.getvalue('TimeZone')
else:
  myTz = "TimeZone undefined"
  error += 1
if form.getvalue('Hour1'):
  myHour1 = form.getvalue('Hour1')
else:
  myHour1 = "Hour1 undefined"
  error += 1
if form.getvalue('Brightness1'):
  myBrightness1 = form.getvalue('Brightness1')
else:
  myBrightness1 = "Brightness1 undefined"
  error += 1
if form.getvalue('Hour2'):
  myHour2 = form.getvalue('Hour2')
else:
  myHour2 = "Hour2 undefined"
  error += 1
if form.getvalue('Brightness2'):
  myBrightness2 = form.getvalue('Brightness2')
else:
  myBrightness2 = "Brightness2 undefined"
  error += 1

print("Content-Type: text/html")
print (
"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width" />
<meta http-equiv="refresh" content="10;URL=/pyClock/">
<link rel='stylesheet' id='dark-css'  href="./style.css" type="text/css" media="all" />
<title>Submitted</title>
</head>
<body>

<H2>Submitted values:</H2>
"""
)
print ("<P>Timezone is %s</P>" % myTz)
print ("<P>Hour1 is %s</P>" % myHour1)
print ("<P>Brightness1 is %s</P>" % myBrightness1)
print ("<P>Hour2 is %s</P>" % myHour2)
print ("<P>Brightness2 is %s</P>" % myBrightness2)
if error == 0 :
  if myTz == myOldTz :
    # kill SIGUSR1
    print ("<P>Sending signal to clock process to run with new hour/brightness values</P>")
  else:
    # systemctl
    print ("<P>Clock system service will now restart with new timezone and new values</P>")
else:
  print ("<P class=rederror>There are ",error," errors, please try again</P>", sep="")
print (
"""
<P>Redirecting to <A HREF="/pyClock/">Clock Control</A> page in 10 seconds...</P>
</body>
</html>
"""
)

if error == 0:
  #write back to ini file
  config['CLOCK'] = { 'Display': '884', 'TimeZone': myTz, 'Hour1': myHour1, 'Brightness1': myBrightness1, 'Hour2': myHour2, 'Brightness2': myBrightness2 }
  with open('/var/lib/pyClock/pyClock.ini', 'w') as configfile:
    config.write(configfile)

  if myTz == myOldTz :
    with open('/var/lib/pyClock/pyClock.pid', 'r') as pidfile:
      myPid = pidfile.read()
      # print('PID: ',str(myPid))
      pidfile.close()
    # send SIGUSR1 to clock to re-read config variables from file
    os.system('/usr/bin/sudo /bin/kill -SIGUSR1 %i' % int(myPid))
  else:
    # restart clock system service via systemctl
    os.system('/usr/bin/sudo /bin/systemctl restart Matrix8Clock')
