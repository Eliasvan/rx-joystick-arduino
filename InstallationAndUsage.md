For an example, look at the [Example wiki](Example.md).


# Setup #

This has to be done only once.

## Hardware ##

### Required components ###

  * [Arduino](http://arduino.cc/en/Main/Products), with an USB cable
> Almost all Arduinos are valid, except if the [RC Receiver Shield](RCReceiverShield.md) is used, some small-scale editions won't fit, such as the Mini, Micro or Nano.

  * RC receiver, with the corresponding transmitter and some extension RC connector cables
> With some newer receiver models, it may not work using the Channel output ports, and may only work using a PPM signal port, if provided.
> If you don't have any extension RC connector cables, you can make one by cutting and stripping the cable of an old/broken servo.

  * Optional but recommended: [Arduino RC Receiver Shield wiki](RCReceiverShield.md)
> If not used, you can manually connect the receiver with the Arduino, as done in the [Example wiki](Example.md).

### Connections ###

You can either choose to use the CHannel ports, or the BATtery (PPM) port of your RC receiver.

The first one requires you to connect all desired channel ports. The second only requires only one cable and will provide all channels available (but is not yet implemented).

First read the next section if you don't use the BAT/PPM port, then read either the **Without RC Receiver Shield** or the **With RC Receiver Shield** section whether or not you have an RC Receiver Shield.

#### Matching the right RC channel header with the right Arduino digital pin / channel on the RC Receiver Shield ####

The amount of channels used, should be 8 or less, and you can even choose to exclude channels in-between on the RC receiver side.
On the Arduino side, all channel numbers have to be contiguous, in order, and start with the first channel.

So, in the case you don't have a RC Receiver Shield, the first "channel" on the Arduino side is digital pin number 2 (D2).

And, if you have a RC Receiver Shield, the first channel on the RC Receiver Shield is Ch1.

_Example:_

> Suppose you have a 10-channel RC receiver, and you want to capture channels 1, 3, 4, 5 and 10.

> Without RC Receiver Shield:
> connect the signal pin of the RC header of channel 1 with D2 on the Arduino, channel 3 with D3, channel 4 with D4, channel 5 with D5 and channel 10 with D6.

> With RC Receiver Shield:
> connect the RC header of channel 1 with Ch1 on the RC Receiver Shield, channel 3 with Ch2, channel 4 with Ch3, channel 5 with Ch4 and channel 10 with Ch5.

#### Without RC Receiver Shield ####

  * Connect the RC receiver with the Arduino using extension RC connector cables:
    1. Connect the `ground` of each RC header (one of the extreme pins, usually with a dark coloured wire) with (one of) the Arduino's "ground" pin(s).
    1. Connect the `Vcc` of each RC header (middle pin, usually with a red coloured wire) with the Arduino's "5V" pin.
    1. If you use the CHannel ports: Connect the `signal` output of each RC header (the other extreme pin, usually with a light coloured wire) with the right Arduino's "D#" (digital) pin, as described in the previous section.
> > If you use the BATtery (PPM) port: Connect the `signal` output of the BAT RC header (the other extreme pin, usually with a light coloured wire) with Arduino's "D8" (digital) pin (, this is the Arduino's capture input pin).
  * Make sure all your connections are well-done, so that there can't be any short-circuit.

_Example_:

Using "CHs" mode and capturing channel 1 and 2 of RC receiver.

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/ConceptTestSetup/setup.png](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/ConceptTestSetup/setup.png)

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/ConceptTestSetup/setup_real.jpg](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/ConceptTestSetup/setup_real.jpg)
![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/ConceptTestSetup/setup_real_zoom.jpg](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/ConceptTestSetup/setup_real_zoom.jpg)

#### With RC Receiver Shield ####

  * Push the shield on the Arduino.
  * Connect the RC receiver with the RC Receiver Shield using extension RC connector cables, as described in two sections before.

> ` `**Warning**: it is important that you choose to use either the "Ch#" input ports **OR** the "BAT" input port (PPM signal), and correspondingly you have to put the switch to either "CHs/PWM" or "BAT/PPM".

_Example_:

Using "CHs" mode and capturing channel 1, 3, 4 and 5 of RC receiver.

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/example_setup2.jpg](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/example_setup2.jpg)
![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/example_setup.jpg](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/RCReceiverShield/example_setup.jpg)

## Software ##

### Arduino side ###

  * Get the latest [Arduino software](http://arduino.cc/en/Main/Software) (your distribution may even have packaged it). This will be used to compile code and flash it on the Arduino's microprocessor.
  * Connect the Arduino with your computer using the USB cable.
  * Open the installed program and load the file "`RC_receiver.ino`" located at "/Software/Arduino/".
  * Click on the upload icon. If all went right, the program should report:
```
Upload done.
```
> This program code will stay on the Arduino, even if it has been powered off.

### Computer side ###

Make sure the following dependencies are installed on your computer:

  * [python](http://www.python.org/download/)
  * [pyserial](http://pypi.python.org/pypi/pyserial)
  * [python-uinput](http://pypi.python.org/pypi/python-uinput)
> This last one only works on Linux, in the future a dummy class will be made to print all received controls, if the python `uinput` module is not found.
  * The `serialToJoystick.py` program, located at "/Software/Computer/"


# Usage #

## Hardware ##

  * Power on the RC transmitter.
  * Connect the Arduino with your computer using the USB cable.

## Software ##

  * Execute the `serialToJoystick.py` program with minimal command-line arguments (Arduino device will be auto-detected, as well as the amount of channels connected, PWM/PPM mode, and period), by running
```
$ python serialToJoystick.py
```
> in that directory, this works on Linux. Note: you may have to execute it with root-permissions (as superuser, e.g.: "`sudo python serialToJoystick.py`"), because it creates an externally accessible virtual joystick device.

> You can also pass some extra options to fit your needs, here is the help message:
```
$ python serialToJoystick.py --help

usage: serialToJoystick.py [-h] [-m, --mode {-1,0,1}]
                           [-c, --num-channels {0,1,2,3,4,5,6,7,8}]
                           [-f, --filtering-fuzz {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}]
                           [-n, --name CONTROLLERNAME]
                           [-d, --device ARDUINODEVICE] [-D, --double-sweep]
                           [-t, --test]

Creates a virtual joystick controller using data from a RC receiver via an
Arduino. Go to http://code.google.com/p/rx-joystick-arduino/ for more info.

optional arguments:
  -h, --help            show this help message and exit
  -m, --mode {-1,0,1}   the type of source we'll be capturing from: '0': use
                        multiple separate PWM channel inputs (from receiver
                        outputs); '1': use one combined PPM input (e.g. from
                        transmitter's D.S.C. output) as input to capture all
                        channels; if not provided or '-1' is used,
                        autodetection will be performed, PWM mode has the
                        highest priority
  -c, --num-channels {0,1,2,3,4,5,6,7,8}
                        the exact amount of channels used, if not provided or
                        '0' is used, autodetection will be performed
  -f, --filtering-fuzz {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
                        the number of adjacent values that are result of
                        quantization noise, if '1' is used, no filtering will
                        be performed; default value is '6'
  -n, --name CONTROLLERNAME
                        the name of the virtual joystick, how it will appear
                        to other applications, if not provided, autogeneration
                        will occur
  -d, --device ARDUINODEVICE
                        the device path of the Arduino, on Linux usually
                        something like '/dev/ttyACM0', if not provided,
                        autodetection will be performed
  -D, --double-sweep    double the range of all channels, resolution will be
                        halved
  -t, --test            print and visualise every controller event update,
                        don't create an externally accessible virtual joystick
```

> _Example on Windows:_

> The following command will visualise (test) controller events with a RC receiver with 2 channels connected to the Arduino (no PPM input). Let's assume we know that the Arduino is located at `COM4`.
```
$ python serialToJoystick.py -c 2 -d COM4 -t
```
> The output will look like:
```
#### Incoming Joystick 'RC Receiver (2chs)' Event: ####
# Axis 0 [--------o--------] 127 (50%)
# Axis 1 [--------o--------] 127 (50%)
```

> Concluding, if all went right, the following message shows up in the terminal, you'll be able to use it (it will show up with the name "`<your joystick name>`") in all games supporting joysticks:
```
Created a joystick device named '<your joystick name>'.
```
  * Start a game or application that uses this joystick, and enjoy!
  * To stop the joystick, send a `KeyboardInterrupt` in the terminal where `serialToJoystick.py` is running by pressing `Ctrl-C`.

### Games, configuration files ###

Joystick configuration files for various applications are released under "`/Software/Computer/ThirdPartyConfigurations/`".
Look in the folder corresponding with an application for the "`Readme.txt`" file to get more info/instructions.

Currently available:
  * Flightgear