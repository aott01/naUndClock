#!/usr/bin/env python3                                                                                             

import cgi, cgitb
form = cgi.FieldStorage()

if form.getvalue('timezone'):
  myTz = form.getvalue('timezone')
else:
  myTz = "timezone undefined"
if form.getvalue('hour1'):
  myHour1 = form.getvalue('hour1')
else:
  myHour1 = "hour1 undefined"
if form.getvalue('bright1'):
  myBright1 = form.getvalue('bright1')
else:
  myBright1 = "bright1 undefined"
if form.getvalue('hour2'):
  myHour2 = form.getvalue('hour2')
else:
  myHour2 = "hour2 undefined"
if form.getvalue('bright2'):
  myBright2 = form.getvalue('bright2')
else:
  myBright2 = "bright2 undefined"

print("Content-Type: text/html")
print(
"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width" />
<link rel='stylesheet' id='dark-css'  href="./style.css" type="text/css" media="all" />
<title>Submitted</title>
</head>
<body>

<P>submitted values: </P>
"""
)
print ("<P>Timezone is %s</P>" % myTz)
print ("<P>Hour1 is %s</P>" % myHour1)
print ("<P>Bright1 is %s</P>" % myBright1)
print ("<P>Hour2 is %s</P>" % myHour2)
print ("<P>Bright2 is %s</P>" % myBright2)


print(
"""

</body>
</html>
"""
)
