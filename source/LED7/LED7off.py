 #!/usr/bin/python3

import syslog

from Adafruit_LED_Backpack import SevenSegment

syslog.syslog("turning off display with LED7off.py")

# ===========================================================================
# turn off display by writing ' ' space to all four segments
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

segment.set_brightness(0)

segment.clear()
segment.set_digit(0, " ")
segment.set_digit(1, " ")
segment.set_digit(2, " ")
segment.set_digit(3, " ")
segment.set_colon(0)

# Write the display buffer to the hardware.  This must be called to
# update the actual display LEDs.
segment.write_display()
