#!/usr/bin/python3
""" This turns off the Matrix8Clock display by writing spaces to it (dark) """

import syslog

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219

syslog.syslog("turning off Matrix8Clock")

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)

virtual = viewport(device, width=32, height=8)

device.contrast(16)	# 0..255

with canvas(virtual) as draw:
  draw.text((1, 0), "        ", fill="white")
