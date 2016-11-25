#!/bin/usr/python
# coding: utf-8

""" Position Calculations for Mechanism Design and Analyses (PCMDA)

Since SOMEONE needs to work the maths behind the curtain... This is for Python2, mind you. Because I <i>care</i>.

MIT-License, y'all. No need to go to jail for this, thank you very much.

"""

# Core libraries
import math
import numpy as np

def GetSteps():
    While True:
        try:
            steps = int(raw_input("Enter the number of steps: "))
            break
        
        except:
            print "You need to supply this programm with the number of steps. Try again!"
    return steps

def GetDistance(x1, y1, x2, y2):
    # Very basic. Fetch me the distance between two points. Pretty please... :'(
    return d = math.sqrt(((x2-x1)**2)*((y2-y1)**2))

def GetLinearActuatorFunction(x_start, y_start, x_end, y_end):
    # Now we are getting lazy. I know, I know... We are starting out linear-ily. Ish.
    
    steps = GetSteps()
    
    x, y, t = [], [], []
    
    for schritt in range(1,steps+1):
        t.append(steps)
        x.append(x_start+(x_end-x_start)*schritt/steps)
        y.append(y_start+(y_end-y_start)*schritt/steps)
    
    f = {'t': t, 'x': x, 'y': y}
    
    return f

def GetPeriodicActuatorFunction(x_start, y_start):
    # And we are going... PERIODICALLY!
    while True:
        try:
            startangle = int(raw_input("Choose the starting position:\n\n1 - Closest to reactant 1\n2 - Maximum distance from reactant1\n3 - Specify degree"))
            break
        except:
            print "Try again. Choose 1, 2 or 3."
    
    if startangle == '1':
        angle == 180
    elif startangle =='2':
        angle == 0
    else:
        while True:
            try:
                angle = int(raw_input("Degrees [°]: "))
                angle = angle%360
                break
            except:
                print "Invalid number. Try again"
    steps = GetSteps()
    x, y = [], []
    for degr in range(0, 360):
        currentdegr = (degr + angle)%360
        t.append(currentdegr)
        x.append(np.cos(currentdegr)+x_start)
        y.append(np.sin(currentdegr)+y_start)
    
    f = {'t': t, 'x': x, 'y': y}
    
    return f
        
    
