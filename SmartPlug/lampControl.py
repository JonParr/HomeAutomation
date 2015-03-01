#/usr/bin/env python

import sys
import time
import socket


if len(sys.argv) != 2:
	print('Insufficient arguments.')
	exit(1)

controlWord = sys.argv[1]

if not (controlWord == 'on' or controlWord == 'off' or controlWord == 'quit'):
	print 'Unknown control character {}'.format(controlWord)
	exit(1)

print 'Sending command: {}'.format(controlWord)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1',8001))
s.send(controlWord)
s.close()

exit(0)