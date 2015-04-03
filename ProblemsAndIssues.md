### "The extension RC connector cables don't fit in the headers of the RC Receiver Shield." ###

First ensure the (female) headers are all soldered in place, that should make the following task easier.
Then, for each header, use a knife to chop off two corners of one side.
**It is important that you choose the right side:**
This side is shown of the PCB images on the [RC Receiver Shield wiki](RCReceiverShield.md).


### "My RC receiver has more than 8 output channels." ###

In that case, if you're planning to use 8 or less channels, it will still work:
you need to connect it with the Arduino in the way described on the InstallationAndUsage wiki.

What follows, assumes you want to effetely use more than 8 channels.

This maximum amount is chosen because the big majority of RC receivers has this amount or less, and then the size and complexity of the RC Receiver Shield remains feasible for DIY purposes.

However, it is technically possible to extend the code on the Arduino-side, computer-side and the RC Receiver Shield hardware, to meet stronger requirements.

But there is a limit:
each channel signal is directly derived from the (internal) PPM signal, which allocates a maximum time of about 2ms (can be even more) and the total PPM period is about 22ms. Keep in mind that on the end of the PPM signal, a sync signal of at least 4ms is needed. That makes a total of (22-4)ms / 2ms = 9 channels. However other modulation techniques/parameters may increase this amount.


### "Everything is set up right, but the computer can't connect with the RC Receiver." ###

Sometimes this problem can be solved by trying to rerun the command.

This can occur when a valid serial(-USB) connection is set up with the Arduino, but the handshake after connection establishment times out.
You may have to increase the `timeout` variable at the Serial object construction in the "serialToJoystick.py" file.


### "Arduino autodetection does not work." ###

The code handling this part is strongly platform dependent (should change in the future).

You can solve this by manually specifying the device-name as an argument in the command-line.


### "If all controls are set to mid-position (or hold steady), there are small alternating variations superposed on the constant output value." ###

This is caused by the timing resolution (granularity => quantization noise) of the Arduino, which is 4us on the 16 MHz editions, and 8us on the 8 Mhz editions. The inverse of this time gives the sampling frequency.

To address this problem, an enhanced fuzz-flat filter is used. The higher the "fuzz" parameter is set, the less noise the output will contain. However, setting this parameter too high, will cause the output to be unresponsive and laggy when the controls are changed.

6 adjacent values of "fuzz", proves to be a good filtering parameter.
If 1 value of "fuzz" is used, the filter doesn't have any effect, so the resulting data is unfiltered.


### "Using PPM output does not work: the peak-to-peak signal is only ~1 Volt (instead of 5 Volts)." ###

You can build a little circuit that cranks the low value up to ~2 Volts or one that cranks the high value up to ~3 Volts.

I needed to do the latter for the Graupner MX-12, and the following circuit is tested and works (although I know it seems counter-intuitive that there is actually 2.2V on the + side of transmitter, that's probably because the model used for the PPM signal source is not exact.)
This is the circuit I used:

![http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/PPMAnalysis/LowVoltageSweepFix_schema.png](http://rx-joystick-arduino.googlecode.com/svn/trunk/Hardware/PPMAnalysis/LowVoltageSweepFix_schema.png)


### "Ok, nice, but where can I download all stuff?" ###

  1. Go to the "`Project Home`" tab above and click on it.
  1. You can **download** a release by clicking below on "`Downloads`" under the `External links` section in the the left navigation area.

It contains all required files for the `Software` and `Hardware` components.