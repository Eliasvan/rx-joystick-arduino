# -*- coding: utf-8 -*-
import serial
import os
import time, math

#debugData = "" # TODO: remove (debug)
packetCounter = 0


#controllerName = "Graupner MX"
controllerName = None

numChannels = 2
arduinoDevice = None
doubleSweep = False
useCompositePPM = False

maxLatency = 100e-3 # 100ms
doFiltering = True
filteringTolerance = 8

PPM_Period = 22e-3



def connectToArduino():
	# TODO: make this OS independant
	global arduinoDevice
	if not arduinoDevice:
		try:
			from serial.tools import list_ports
			dmesgOutput = os.popen('dmesg').read()
			lastOccurence = dmesgOutput.rfind("Arduino")
			ttyBegin = dmesgOutput.find("tty", lastOccurence)
			ttyEnd = min([dmesgOutput.find(c, ttyBegin) for c in (':', ' ', '\t', '\r', '\n') if c in dmesgOutput[ttyBegin:]])
			arduinoDevice = list(list_ports.grep(dmesgOutput[ttyBegin:ttyEnd]))[0][0]
		except:
			print ("Could not automatically find your Arduino device.")
	
	ser = serial.Serial(
			port = arduinoDevice,
			baudrate = 9600,
			bytesize = serial.EIGHTBITS,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			timeout = 1,
			xonxoff = 0,
			rtscts = 0,
			interCharTimeout = None
		)
	
	print ("Connected to Arduino at '%s'." % arduinoDevice)
	
	return ser


def connectToRCreceiver(ser):
	command = ((numChannels-1) << 2) + (doubleSweep << 1) + useCompositePPM
	
	numRetries = 4
	for i in range(numRetries):
		ser.write(chr(command) + "\n")
		response = ser.readline()
		valid = (len(response) == 1 + 2 and response == chr(command) + "\r\n") # echo command + CR + NL
		if valid:
			break
	
	if not valid:
		print ("Failed to connect to RC receiver via Arduino on '%s'." % arduinoDevice)
		return False
	
	print ("Connected to RC receiver. (%s channels via %s)" % \
			(numChannels, ("channel connectors", "battery connector")[useCompositePPM]))
	
	return True


def createJoystick():
	global controllerName
	if not controllerName:
		controllerName = "RC Receiver (%schs)" % numChannels
	events = [(3, i) + (0, 255, 0, 0) for i in range(numChannels)]
	
	try:
		import uinput
		joy = uinput.Device(events, name = controllerName, bustype = 0x03) # bustype = BUS_USB
		#writeJoystick(joy, chr(128) * numChannels)
	except OSError:
		print ("Failed to create a joystick device.")
		return None
	
	print ("Created a joystick device named '%s'." % controllerName)
	
	return joy


def readRCreceiver(ser, joy):
	#global debugData # TODO: remove (debug)
	global packetCounter
	buffer = ""

	dataSize = numChannels + 1 # 1: sep = '\xff'
	maxBuffer = math.ceil(dataSize * maxLatency/PPM_Period)

	while True:
		if ser.inWaiting() > maxBuffer:
			ser.flushInput()
			buffer = ""
			print "Buffer overrun occured. Resetting buffer."
		
		#time.sleep(20e-3 / 2) # 20ms / 2
		if ser.inWaiting():
			newData = ser.read(ser.inWaiting())
		else:
			newData = ser.read() # block cpu
		buffer += newData
		#debugData += newData # TODO: remove (debug)
		if '\xff' in buffer:
			data, buffer = buffer.split('\xff')[-2:]
			if len(data) == numChannels:
				writeJoystick(joy, processData(data))
				packetCounter += 1
			#print data # TODO: remove (debug)


lastlastData = numChannels * [127]
lastData     = numChannels * [127]
holdLastData = numChannels * [False]
def processData(data):
	global lastlastData, lastData, holdLastData
	data = list(data)
	#unf = list(data)
	for i, d in enumerate(data):
		data[i] = ord(d) - 1
		if data[i] >= 253:
			data[i] = 255
		#unf[i] = data[i]
		# Filtering of arduinos timing granularity at a frequency of about 45Hz
		if doFiltering:
			if holdLastData[i]:
				holdLastData[i] = (data[i] == lastData[i])
				if abs(data[i] - lastData[i]) < filteringTolerance:
					data[i] = lastData[i]
			elif data[i] == lastlastData[i]:
				holdLastData[i] = True
	lastlastData = lastData
	lastData = data
	#print data, unf
	return data


def writeJoystick(joy, data):
	for i in range(numChannels):
		joy.emit((3, i), data[i], syn = (i == numChannels-1))
		#print "joy.emit((3, %s), %s, syn = %s)" % (i, data[i], i == numChannels-1) # TODO: remove (debug)


def main():
	ser = joy = None

	try:
		ser = connectToArduino()
		if connectToRCreceiver(ser):
			joy = createJoystick()
			if joy:
				startTime = time.time()
				readRCreceiver(ser, joy)
	
	except serial.serialutil.SerialException:
		print ("Failed to connect to Arduino on '%s'." % arduinoDevice)
	
	except KeyboardInterrupt:
		pass
	
	finally:
		endTime = time.time()
		
		if ser:
			ser.close()
		
		#print debugData.split("\xff") # TODO: remove this
		#packetCounter = len(debugData.split("\xff")) # TODO: remove this
		if joy:
			#print "Time of CPU:", endTime - startTime # TODO: remove this
			expectedNbPackets = (endTime-startTime) / PPM_Period
			print ("%s packets captured (%s%%)" % (packetCounter, int(100 * packetCounter/expectedNbPackets)))
		
		print ("Connections closed.")

if __name__ == "__main__":
	main()