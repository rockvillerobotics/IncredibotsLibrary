from wallaby import *
import constants as c

#-------Accessors-----
# These give the value of the sensor plugged in the "port" slot.
# Must run "camera_open()" and wait ~2 seconds before using webcam.
 
def get_tophat(port):
    return(analog(port))

def get_gyro():
    return(gyro_z())

def get_limit(port):
    return(digital(port))

def get_depth(port):
    return(analog(port))

def get_webcam(channel):
    camera_update()
    return(get_object_area(channel, 0))
    
            
#-------Tophat--------

# Tells if the tophat in the "port" slot senses black.
# The "value_midpoint" is some value between the values detected for black 
# and white. This is used to differentiate between the two. Normally ~2000. 
def senses_black(port, value_midpoint):
    return(analog(port) > value_midpoint)
        
# Line follows will the tophat in the "port" slot for "time" milliseconds.
# "value_midpoint" is usually around 2000.
def line_follow(port, value_midpoint, time):
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if senses_black(port, value_midpoint):
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 1000)
        else:
            mav(c.LEFT_MOTOR, 1000)
            mav(c.RIGHT_MOTOR, 0)
        msleep(30)

# This file contains sensor algorithims.