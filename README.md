Based on https://github.com/google/OctoPrint-LEDStripControl

# Octoprint-hyperion

## Hardware/Software prerequisits

You need some kind of ws2812 ring/ribbon. (e.g. https://www.aliexpress.com/item/1pcs-RGB-LED-Ring-24Bit-WS2812-5050-RGB-LED-Integrated-Drivers/32673245219.html)

At first you need to have this working without octoprint. Octoprint will just use Mxxx gcode to execute hyperion-remote commands to drive the leds. You can then do whatever effect you want (like k2000 or snake) and even command any other remote hyperion instance (e.g. Ambilight in you TV).

I use a ring of 24 leds in 5v and I just connect the 3 pins to the raspberry without external power (I know that this is not best practice). More leds would require external power for sure (or if you use 12V strip).

For the pin, just +5, gnd and gpio 16 is the default. In "pin numbers" this is 2, 6 and 12.

Led ring support :
https://www.thingiverse.com/thing:2503909

#### Hyperion install on PI:

The easy way is to use Hypercon -> here -> https://hyperion-project.org/wiki/HyperCon-Information
When you have it, configure the ssh to point to your raspberry. Put Ip, username, password and chose "All systems".
When you click Inst./Upd. Hyperion, everything will be installed and PI will reboot.

#### Hyperion led ring device configuration

After reboot, you will have to edit the configuration file to configure the leds (can be done with hypercon if you want):

Put this in the device section :

	// DEVICE CONFIGURATION
	"device" :
	{
		"name"       : "Octoprint",
		"type"       : "ws281x",
		"leds"     : 24,
		"dmanum"  : 10,
		"colorOrder" : "grb"
	},

#### Testing

Restart the hyperion deamon:

sudo service hyperion restart

Check the start logs :

journalctl -u hyperion.service


Check that it is working with:

hyperion-remote -e "Snake"

Or

hyperion-remote -c blue

And switch off with

hyperion-remote -x


## Drive hyperion lights via MXXX commands

You need to add the require MXXX command in your gcode or type it directely in the octoprint terminal.

Example :

- White lightning:
    M150 -c FFFFFF
- Lights off:
    M150 -x
- Start effect (keep the quote in the command):
    M150 -e "Snake"

Usefull command args are -e ; -x ; -c

Hyperion command line :

Usage: hyperion-remote [OPTIONS]

Parameters:
-  -c, --color <arg>
-  -e, --effect <arg>
-  -x, --clear
-  --clearall

Effect list :

- Cinema brighten lights
- Cinema dim lights
- Knight rider
- Blue mood blobs
- Cold mood blobs
- Full color mood blobs
- Green mood blobs
- Red mood blobs
- Warm mood blobs
- Police Lights Single
- Police Lights Solid
- Rainbow mood
- Rainbow swirl fast
- Rainbow swirl
- Random
- Running dots
- System Shutdown
- Snake
- Sparks Color
- Sparks
- Strobe blue
- Strobe Raspbmc
- Strobe white
- Color traces
- X-Mas   
