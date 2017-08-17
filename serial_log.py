#!/usr/bin/python
# Get lines of text from serial port, save them to a file.

import datetime
import os
import serial
import sys

addr      = '/dev/ttyUSB0'                   # serial port to read data from
baud      = 128000                           # baud rate for serial port
date      = datetime.datetime.now()
directory = 'logs'
fname     = 'log_' + str(date) + '.txt'  # log file to save data in
fmode     = 'w'                              # log file mode = APPEND

if not os.path.exists(directory):
    os.makedirs(directory)

with serial.Serial(addr, baud) as ser, open(directory + '/' + fname, fmode) as f:
    while (1):
        x = ser.read()         # read one line of text from serial port
        sys.stdout.write(x)    # echo byte on-screen as ASCII
        sys.stdout.flush()     # make sure it actually gets written out
        f.write(x)             # write line of text to file
        f.flush()              # make sure it actually gets written out