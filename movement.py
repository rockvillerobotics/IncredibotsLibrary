from wallaby import *
import constants as c


# Drives forward for "time" milliseconds (1000 ms = 1 s).
def drive(time):
    mav(c.LEFT_MOTOR, 1000)
    mav(c.RIGHT_MOTOR, 1000)
    msleep(time)
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)

# Backs up for "time" milliseconds.
def back_up(time):
    mav(c.LEFT_MOTOR, -1000)
    mav(c.RIGHT_MOTOR, -1000)
    msleep(time)
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)

# Turns left for "time" milliseconds. ~900 ms is a 90 degree turn.
def turn_left(time):
    mav(c.LEFT_MOTOR, -1000)
    mav(c.RIGHT_MOTOR, 1000)
    msleep(time)
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)
        
# Turns right for "time" milliseconds. ~900 ms is a 90 degree turn.
def turn_right(time):
    mav(c.LEFT_MOTOR, 1000)
    mav(c.RIGHT_MOTOR, -1000)
    msleep(time)
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)


# ~~~~~~~ SERVOS ~~~~~~~
# Make sure to "enable_servo(SERVO_PORT)" for each servo to turn them all on!
# Also, make sure your servos are plugged in the right direction
# (From closest to screen: Orange, Red, Brown) or it won't work.

# Moves servo to "pos" position. Catches destructive values. 
def set_pos(port, pos):
    if(pos > 2047):
        pos = 2047
    elif(pos < 0):
        pos = 0
    set_servo_position(port, pos)

#---------------------------------------------------
# RENAME THIS METHOD                                |
# This is a more effective way to move servos as    |
# it gives more leverage and breaks servos less.    |
#---------------------------------------------------
# Moves servo to "pos" position at "speed" units / millisecond. ~15 is a standard speed.
def set_pos_advanced(port, pos, speed):
    if(pos > 2047):
        pos = 2047
    elif(pos < 0):
        pos = 0
    current_pos = get_servo_position(port)
    while(current_pos + speed < pos or current_pos - speed > pos):
        set_servo_position(port, current_pos)
        if(pos - get_servo_position(port) < 0):
            current_pos -= speed
        elif(pos - get_servo_position(port) > 0):
            current_pos += speed
        msleep(10)
    # This ensures that the exact pos is reached. The unit change will be less than "speed".
    set_servo_position(port, pos)  
    

# This file contains basic movement and servo usage.