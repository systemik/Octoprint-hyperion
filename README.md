# Octoprint-hyperion
Drive hyperion lights via M150 commands

Usefull command args are -e ; -x ; -c


Hyperion command line :

hyperion-remote:
	version   : V1.03.3 (brindosch-2fbbcff/2f01dfa-1495880388
	build time: Jun  3 2017 02:06:16
Simple application to send a command to hyperion using the Json interface
Build time: Jun  3 2017 02:06:13

Usage: hyperion-remote [OPTIONS]

Parameters:
    -a, --address <arg>          Set the address of the hyperion server [default: localhost:19444]
    -p, --priority <arg>         Use to the provided priority channel (the lower the number, the higher the priority) [default: 100]
    -d, --duration <arg>         Specify how long the leds should be switched on in millseconds [default: infinity]
    -c, --color <arg>            Set all leds to a constant color (either RRGGBB hex value or a color name. The color may be repeated multiple time like: RRGGBBRRGGBB)
    -i, --image <arg>            Set the leds to the colors according to the given image file
    -e, --effect <arg>           Enable the effect with the given name
        --effectArgs <arg>       Arguments to use in combination with the specified effect. Should be a Json object string.
    -l, --list                   List server info and active effects with priority and duration
    -x, --clear                  Clear data for the priority channel provided by the -p option
        --clearall               Clear data for all active priority channels
    -q, --qualifier <arg>        Identifier(qualifier) of the transform to set
    -s, --saturation <arg>       !DEPRECATED! Will be removed soon! Set the HSV saturation gain of the leds
    -v, --value <arg>            !DEPRECATED! Will be removed soon! Set the HSV value gain of the leds
    -u, --saturationL <arg>      Set the HSL saturation gain of the leds
    -m, --luminance <arg>        Set the HSL luminance gain of the leds
    -n, --luminanceMin <arg>     Set the HSL luminance minimum of the leds (backlight)
    -g, --gamma <arg>            Set the gamma of the leds (requires 3 space seperated values)
    -t, --threshold <arg>        Set the threshold of the leds (requires 3 space seperated values between 0.0 and 1.0)
    -b, --blacklevel <arg>       !DEPRECATED! Will be removed soon! Set the blacklevel of the leds (requires 3 space seperated values which are normally between 0.0 and 1.0)
    -w, --whitelevel <arg>       !DEPRECATED! Will be removed soon! Set the whitelevel of the leds (requires 3 space seperated values which are normally between 0.0 and 1.0)
        --print                  Print the json input and output messages on stdout
    -h, --help                   Show this help message and exit
    -y, --qualifier <arg>        !DEPRECATED! Will be removed soon! Identifier(qualifier) of the correction to set
    -Y, --correction <arg>       !DEPRECATED! Will be removed soon! Set the correction of the leds (requires 3 space seperated values between 0 and 255)
    -z, --qualifier <arg>        Identifier(qualifier) of the temperature correction to set
    -Z, --temperature <arg>      Set the temperature correction of the leds (requires 3 space seperated values between 0 and 255)
    -j, --qualifier <arg>        Identifier(qualifier) of the adjustment to set
    -R, --redAdjustment <arg>    Set the adjustment of the red color (requires 3 space seperated values between 0 and 255)
    -G, --greenAdjustment <arg>  Set the adjustment of the green color (requires 3 space seperated values between 0 and 255)
    -B, --blueAdjustment <arg>   Set the adjustment of the blue color (requires 3 space seperated values between 0 and 255)
    
Effect list :
    
Cinema brighten lights
Cinema dim lights
Knight rider
Blue mood blobs
Cold mood blobs
Full color mood blobs
Green mood blobs
Red mood blobs
Warm mood blobs
Police Lights Single
Police Lights Solid
Rainbow mood
Rainbow swirl fast
Rainbow swirl
Random
Running dots
System Shutdown
Snake
Sparks Color
Sparks
Strobe blue
Strobe Raspbmc
Strobe white
Color traces
UDP listener
X-Mas
    