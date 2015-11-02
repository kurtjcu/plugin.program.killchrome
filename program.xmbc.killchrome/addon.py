import xbmcaddon
import xbmcgui
import subprocess
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello World!"
line2 = "We will now destroy chrome"
line3 = "Using Python to run a command in shell"
 
#xbmcgui.Dialog().ok(addonname, line1, line2, line3)



try:
	subprocess.call(['xdotool search --name chrome windowkill'],shell=True)
except:
    log('ERROR executing script killChrome')