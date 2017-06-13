# RasPi-timelapse
Python code to make time-lapse videos.
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
