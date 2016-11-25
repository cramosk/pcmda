#!/bin/usr/python
# coding: utf-8

""" Position Calculations for Mechanism Design and Analyses (PCMDA)

Since SOMEONE needs to work the maths behind the curtain... This is for Python2, mind you. Because I <i>care</i>.

MIT-License, y'all. No need to go to jail for this, thank you very much.

"""

# Core libraries
import math


def GetDistance(x1, y1, x2, y2):
    # Very basic. Fetch me the distance between two points. Pretty please... :'(
    return d = math.sqrt(((x2-x1)**2)*((y2-y1)**2))

def GetLinearActuatorFunction(x_start, y_start, x_end, y_end):
    # Now we are getting lazy. I know, I know... We are starting out linear-ily. Ish.
    While True:
        try:
            steps = int(raw_input("Enter the number of steps: "))
            break
        
        except:
            print "You need to supply this programm with the number of steps. Try again!"
    x, y, t = [], [], []
    
    for schritt in range(1,steps+1):
        t.append(steps)
        x.append()
