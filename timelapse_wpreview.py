###### timelapse_wpreview.py ######
# based on https://www.raspberrypi.org/learning/timelapse-setup/worksheet/
# extras added by George Price 5/21/2017
# Create timelapse video.  User will be prompted
# to input filename, number of frames, and delay
# between frames.
###### NOTICE ######
# 1. This code is written for Python 3.
# 2. Be sure your camera is enabled in your Pi's settings.
# 3. If your camera isn't fully plugged in, you'll get some
#    odd errors.  Make sure it is.
###### STATUS ######
# Some things don't work yet.  I'm still figuring out:
# 1.  how to create an empty folder to put the images in
# 2.  how to create a log file to contain the final report
# 3.  how to play .WAV sounds from within Python
# 5.  Ctrl-C doesn't abort until the sleep() times out.
# 5a. Whatever key aborts, it shouldn't without confirming first.
# 
# I hope you enjoy this as much as I did.
#################################################

from picamera import PiCamera
from os import system
import time
from time import sleep

# these are part of alert sounds experiment, not used yet
#import pyaudio
#import wave



camera = PiCamera()

camera.resolution = (1024, 768) # one of many resolutions available

TLfile=input("What would you like to call the finished GIF?  ")
TLfolder=TLfile  #name the folder after the GIF
TLlongfile="./" + TLfolder + "/" + TLfile + ".GIF"
print(TLlongfile)
numFrames=int(input("How many frames?  "))
numSecs=numFrames/30
numDelay=int(input("How many seconds between frames?  "))
commentString=input("Any comments for the log file?  ")

print("1 frame every", numDelay, "seconds at", camera.resolution, "for",numFrames,"frames.")
print("At 30 fps that will make a", numSecs, "second video.")
epsecsNow = round(time.time())  #Time now in seconds since epoch
epsecsDone = epsecsNow + numFrames*numDelay #Job length in epoch seconds
timeEstimate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epsecsDone))
print("Photography should finish about", timeEstimate)
print("If you're running headless (VNC), you won't see a preview. \n \
      That is normal.  Preview only shows on a connected monitor. \n")
    
alertsounds = str(input("Do you want alert sounds (Y/N)?  "))
print("Starting now.  Ctrl-C to abort.")
localtime = time.localtime()
epsecs = time.time()

numDelay=numDelay-5  #compensate for camera stabilization, 5 seconds
localtime = time.localtime()
timeStart=time.strftime("%Y-%m-%d %H:%M:%S", localtime)


#### Main Camera Loop ####
for i in range(numFrames):
    camera.start_preview()
    sleep(5)
    camera.capture(TLfolder+'image{0:04d}.jpg'.format(i))
#   Use one of the built-in sounds to indicate shutter snap (doesn't work yet)
#   if alertsounds == 'y' or 'Y'
#      system.aplay /usr/share/scratch/Media/Sounds/Percussion/HandClap.wav
    camera.stop_preview()
    print(i+1, "of", numFrames)
    sleep(numDelay)
localtime = time.localtime()
timeStop=time.strftime("%Y-%m-%d %H:%M:%S", localtime)
#if alertsounds == 'y' or 'Y':
#   print("alertsounds =", alertsounds) # just for debugging
#   system.aplay /usr/share/scratch/Media/Sounds/Percussion/Gong.wav
print("Images completed. \n" \
      "Predicted time:  ", timeEstimate, '\n', \
      "Actual time:     ", timeStop, '\n')

#### Conversion section ####
#print("Beginning conversion...")
#system("convert -delay 10 -loop 0 image*.jpg animation.gif")
#localtime = time.localtime()
#timeConv=time.strftime("%Y_%m_%d_%H.%M.%S", localtime)

#### Final Report ####
# I want this to show on the screen AND be saved to the logfile.
print("Filename: ", TLfile + ".GIF")
print('\n', \
      "Started:  ", timeStart, '\n', \
      "Finished: ", timeStop, '\n', \
#      "Converted:", timeConv, '\n\n', \  # IF the .GIF conversion was requested
      "Comments: ", commentString, \
)

#### just for debugging
# system.exit()
