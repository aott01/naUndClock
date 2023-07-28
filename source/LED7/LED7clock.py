#!/usr/bin/python3

import time
import datetime
import syslog

from Adafruit_LED_Backpack import SevenSegment

syslog.syslog("starting LED7clock.py")

# ===========================================================================
# Clock with 24-hr time, brightness dims during the night
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

# brightnes 0...15
segment.set_brightness(5)

# Continually update the time on a 4 char, 7-segment display
while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second

  if hour > 20 :
    segment.set_brightness(0)
  elif hour < 6:
    segment.set_brightness(0)
  elif hour > 6 :
    segment.set_brightness(5)

  segment.clear()
  # Set hours
  segment.set_digit(0, int(hour / 10))     # Tens
  segment.set_digit(1, hour % 10)          # Ones
  # Set minutes
  segment.set_digit(2, int(minute / 10))   # Tens
  segment.set_digit(3, minute % 10)        # Ones
  # Toggle colon
  segment.set_colon(second % 2)              # Toggle colon at 1Hz

  # Write the display buffer to the hardware.  This must be called to
  # update the actual display LEDs.
  segment.write_display()

  # Wait a quarter second (less than 1 second, to prevent colon blinking getting
  # delayed by other processes on single core CPU)
  time.sleep(0.25)

#try to log on exit
syslog.syslog("exiting LED7clock.py")
