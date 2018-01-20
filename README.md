Based on https://github.com/google/OctoPrint-LEDStripControl

# Octoprint-hyperion

## Drive hyperion lights via MXXX commands

You need to add the require MXXX command in your gcode or type it directely in the octoprint terminal.

Example : 

White lightning:
    M150 -c FFFFFF
Lights off:
    M150 -x
Start effect (keep the quote in the command):
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