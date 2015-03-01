#/usr/bin/env python

import serial
import sys
import time
import socket
import os

pid = os.fork()

if pid:
	print 'Daemon forked with PID {}'.format(pid)
	exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1',8001))

s.listen(5)

# Now start the serial connection
serialConnection = serial.Serial('/dev/tty.usbmodem1411',9600,timeout=2)

if not serialConnection.isOpen():
	print 'error: unable to open connection to lamp'
	s.close()
	exit(1)

time.sleep(3)

def commandToCharacter(commandString):
	if chunks == 'on':
		return '1'
	elif chunks == 'off':
		return '0'
	else:
		print 'Unknown command string {}'.format(commandString)
		return '!'

def sendCommand(serialConnection, commandString):

	controlCharacter = commandToCharacter(commandString)

	if controlCharacter == '!':
		return False

	serialConnection.write(controlCharacter)
	serialConnection.flush()

	count = 5;

	while  serialConnection.inWaiting() == 0:
		print 'InWaiting {}'.format(serialConnection.inWaiting())
		time.sleep(1)
		count -= 1
		if not count:
			break

	if not count:
		print('error: unable to obtain response - took too long.')
		return False
	else:
		print ('Response: {}'.format(serialConnection.readline()))
		return True

# Now begin processing any client connections
while True:
	(client,addr) = s.accept()

	chunks = []
	bytes_recd = 0

	while True:
		chunk = client.recv(1)
		if chunk == '':
			break
		chunks.append(chunk)
		bytes_recd += 1

	chunks = ''.join(chunks)

	print 'Received: {}'.format(chunks)

	if chunks == 'quit\n':
		print 'Goodbye'
		break;

	if not sendCommand(serialConnection, chunks):
		print 'An error occurred processing command from client'
	else:
		print 'OK'

serialConnection.close()
s.close()

