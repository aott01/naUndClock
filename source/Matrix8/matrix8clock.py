#!/usr/bin/python3
"""systemd service to drive 8x8 matrix LED clock"""

# sudo mkdir -p /var/lib/pyClock/ && sudo chown pi:www-data /var/lib/pyClock/ \
#    && sudo chmod 775 /var/lib/pyClock/
# sudo chown pi:www-data /var/lib/pyClock/pyClock.ini

import os
import signal
import socket
import time
import syslog
import configparser

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core import legacy
from luma.core.legacy.font import proportional, LCD_FONT

syslog.syslog("starting Matrix8Clock")

with open('/var/lib/pyClock/pyClock.pid', 'w') as pidfile:
  pidfile.write(str(os.getpid()))
  pidfile.close()
with open('/var/lib/pyClock/pyClock.pid', 'r') as pidfile:
  myPid = pidfile.read()
#  print('PID: ',str(myPid))
  syslog.syslog("Matrix8Clock running as pid="+myPid)
  pidfile.close()

config = configparser.ConfigParser()
#config['CLOCK'] = { 'Display': '884', 'TimeZone': 'UTC', 'Hour1': '12', 'Brightness1': '64', 'Hour2': '23', 'Brightness2': '2' }
#with open('/var/lib/pyClock/pyClock.ini', 'w') as configfile:
#  config.write(configfile)
config.read('/var/lib/pyClock/pyClock.ini')
clockconfig = config['CLOCK']
def readConfigFile(clockconfig):
  """reads config file in /var/lib/pyClock/"""
  clockconfig = config['CLOCK']
  config.read('/var/lib/pyClock/pyClock.ini')
  #__DEBUG__
  #print (clockconfig['Display'])
  #print (clockconfig['TimeZone'])
  #print (clockconfig['Hour1'])
  #print (clockconfig['Brightness1'])
  #print (clockconfig['Hour2'])
  #print (clockconfig['Brightness2'])

# from https://stackabuse.com/handling-unix-signals-in-python/
def receiveSignal(signalNumber, frame):
  """generic signal receiver"""
#  print('Received SIG:', signalNumber)
  return
def readConfiguration(signalNumber, frame):
  """SIGHUP signal receiver"""
#  print ('(SIGHUP) re-reading configuration')
  readConfigFile(clockconfig)
  syslog.syslog("Matrix8Clock re-reading config file after SIGUSR1")
#__DEBUG__
#  syslog.syslog(
#    "Matrix8Clock __DEBUG__ values "+str(clockconfig['TimeZone'])+str(clockconfig['Hour1'])\
#    +str(clockconfig['Brightness1'])+str(clockconfig['Hour2'])+str(clockconfig['Brightness2']))
  return

if __name__ == '__main__':
# register the signals to be caught
  signal.signal(signal.SIGUSR1, readConfiguration)
#  signal.signal(signal.SIGUSR2, receiveSignal)

readConfigFile(clockconfig)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)

device.contrast(8)      # 0..255

gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()
#print ("IP:", ipaddr, " GW:", gateway, " Host:", host)
legacy.show_message(device, "Clock Control http://"+ipaddr+"/pyClock/", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)

#read and use clock timezone from ini file
zonename = clockconfig['TimeZone']
os.environ["TZ"] = clockconfig['TimeZone']
syslog.syslog("Matrix8Clock: timezone from ini file is "+zonename)
legacy.show_message(device, "time display in "+zonename, fill="white", font=proportional(LCD_FONT), scroll_delay=0.04)

# loop and check for NTP sync
# /bin/systemctl status systemd-timesyncd.service|/bin/grep -q "Status:..Synchronized to time server"
# one time shot, 1 second delay, then try again
ret = os.system('/bin/systemctl status systemd-timesyncd.service|/bin/grep -q "Status:..Synchronized to time server"')
if ret > 0:
  syslog.syslog("Matrix8Clock: NTP sync return is "+str(ret))
  legacy.show_message(device, "waiting for NTP sync...   ", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
  time.sleep(1)
else:
  ret = os.system('/bin/systemctl status systemd-timesyncd.service|/bin/grep -q "Status:..Synchronized to time server"')
  legacy.show_message(device, "NTP synced", fill="white", font=proportional(LCD_FONT), scroll_delay=0.03)
  syslog.syslog("Matrix8Clock: NTP sync return is "+str(ret))

# example PST8PDT zone values: dark >=20, dark <=6, bright >=7
#       Brightness2 >=Hour2, Brightness2 <Hour1, Brighttness1 >=Hour1
#       default dark
# UTC zone values: dark >=4, bright >=14
#       default bright
device.contrast(int(clockconfig['Brightness1']))
while True:
  with canvas(device) as draw:
    if int(clockconfig['Hour2']) >= int(clockconfig['Hour1']):
      if (int(time.strftime("%k")) >= int(clockconfig['Hour1'])) and (int(time.strftime("%k")) < int(clockconfig['Hour2'])):
        device.contrast(int(clockconfig['Brightness1']))
      if int(time.strftime("%k")) >= int(clockconfig['Hour2']):
        device.contrast(int(clockconfig['Brightness2']))
      elif (int(time.strftime("%k")) < int(clockconfig['Hour1'])) and (int(time.strftime("%k")) <= int(clockconfig['Hour2'])):
        device.contrast(int(clockconfig['Brightness2']))
    else:
      if int(time.strftime("%k")) >= int(clockconfig['Hour1']):
        device.contrast(int(clockconfig['Brightness1']))
      elif int(time.strftime("%k")) >= int(clockconfig['Hour2']):
        device.contrast(int(clockconfig['Brightness2']))
      elif int(time.strftime("%k")) < int(clockconfig['Hour2']):
        device.contrast(int(clockconfig['Brightness1']))
# actual clock is here ;-) , the "blinking colon" is alternating between apostrophe and comma
    if int(time.time()) % 2 == 0:
      now = time.strftime(" %H'%M ")
    else:
      now = time.strftime(" %H,%M ")

    legacy.text(draw, (0, 0), now, fill="white", font=proportional(LCD_FONT))
    time.sleep(0.25) # "blinking colon"
