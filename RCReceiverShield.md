# Introduction #

This page contains information to create an Arduino shield connecting the Arduino with the RC receiver.
There are two editions of this shield: one with the battery connector coming first, the other with the battery connector coming last.
You can choose which one you take, but it's best to take a look at your receiver and use that order, in this way the connector cables will all have about the same length.

The software used to create all material is Fritzing 7.12 (open-source).

### Schematic ###

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryLastConnector/pictures/PCB_schema.png](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryLastConnector/pictures/PCB_schema.png)

### PCB ###

Gerber files are provided to produce the PCB.
The components to be placed on the PCB are listed in "/Hardware/RCReceiverShield/PCB\_bom.html".

On the pictures you can see blue lines at the corners of each RC "Ch" header, the header's corners should be chopped off by cutting along these lines. In that way, the connector cables will fit.

The design places all routes on the bottom of the PCB, (there are no VIAs used,) however double sided print is still needed to solder the Arduino headers. Through-hole metallisation is recommended for the drills of the Arduino headers, but if you're unable to do that, first solder the header in place like you would normally do, then pull the plastic header socket almost (!important!) completely off the pins, afterwards solder the other side (the solder layer on every pin must have the same thickness), finally push the plastic header socket back in place until it reaches this solder layer.

# "Battery connector coming first" edition #

Files are located at "/Hardware/RCReceiverShield/batteryFirstConnector/".

Bottom and Top:

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryFirstConnector/pictures/PCB_pcb_bottom_top.png](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryFirstConnector/pictures/PCB_pcb_bottom_top.png)

Realisation:

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryFirstConnector/pictures/PCB_top_real.jpg](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryFirstConnector/pictures/PCB_top_real.jpg)

Unfortunately in my example the switch is inverted, however a normal switch should just be slided in the direction of the desired mode ("CHs" or "BAT").


# "Battery connector coming last" edition #

Files are located at "/Hardware/RCReceiverShield/batteryLastConnector/".

Bottom and Top:

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryLastConnector/pictures/PCB_pcb_bottom_top.png](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/batteryLastConnector/pictures/PCB_pcb_bottom_top.png)