#!/usr/bin/env python3

import cgi, cgitb
form = cgi.FieldStorage()

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
<title>Clock Control</title>
</head>
<body>
<H2>Clock Control</H2>

<P>Snake languages are at work here</P>

<form action="/LED7clock/submit.py" method="post" target="_blank">
This clock runs in <select name="timezone">
<option value="HST">Hawaii</option>
<option value="US/Alaska">Alaska</option>
<option value="PST8PDT" selected>Pacific</option>
<option value="MST7MDT">Mountain</option>
<option value="CST6CDT">Central</option>
<option value="EST5EDT">Eastern</option>
<option value="UTC">UTC</option>
</select> timezone
<br>
Set brightness of display to value
<select name="bright1">
<option value="0">0</option>
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
<option value="5" selected>5</option>
<option value="6">6</option>
<option value="7">7</option>
<option value="8">8</option>
<option value="9">9</option>
</select>
at
<select name="hour1">
<option value="0">00:00</option>
<option value="1">01:00</option>
<option value="2">02:00</option>
<option value="3">03:00</option>
<option value="4">04:00</option>
<option value="5">05:00</option>
<option value="6">06:00</option>
<option value="7" selected>07:00</option>
<option value="8">08:00</option>
<option value="9">09:00</option>
<option value="10">10:00</option>
<option value="11">11:00</option>
<option value="12">12:00</option>
<option value="13">13:00</option>
<option value="14">14:00</option>
<option value="15">15:00</option>
<option value="16">16:00</option>
<option value="17">17:00</option>
<option value="18">18:00</option>
<option value="19">19:00</option>
<option value="20">20:00</option>
<option value="21">21:00</option>
<option value="22">22:00</option>
<option value="23">23:00</option>
</select>
 hours.
<br>
Set brightness of display to value
<select name="bright2">
<option value="0" selected>0</option>
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
<option value="5">5</option>
<option value="6">6</option>
<option value="7">7</option>
<option value="8">8</option>
<option value="9">9</option>
</select>
at
<select name="hour2">
<option value="0">00:00</option>
<option value="1">01:00</option>
<option value="2">02:00</option>
<option value="3">03:00</option>
<option value="4">04:00</option>
<option value="5">05:00</option>
<option value="6">06:00</option>
<option value="7">07:00</option>
<option value="8">08:00</option>
<option value="9">09:00</option>
<option value="10">10:00</option>
<option value="11">11:00</option>
<option value="12">12:00</option>
<option value="13">13:00</option>
<option value="14">14:00</option>
<option value="15">15:00</option>
<option value="16">16:00</option>
<option value="17">17:00</option>
<option value="18">18:00</option>
<option value="19">19:00</option>
<option value="20" selected>20:00</option>
<option value="21">21:00</option>
<option value="22">22:00</option>
<option value="23">23:00</option>
</select>
 hours.
<br>
The preset values are suggestions for Pacific, Mountain, Central or Eastern timezone. If you select UTC you
+need to compensate for the time offset yourself or maybe select the same brightness for both times.
<br>
<input type="submit" value="Submit"/>
</form>

</body>
</html>
"""
)
