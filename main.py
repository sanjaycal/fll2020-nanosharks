#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
leftmotor = Motor(Port.B)
rightmotor = Motor(Port.C)

time = StopWatch()

rightColor = ColorSensor(Port.S2)
leftColor = ColorSensor(Port.S3)

gyro = GyroSensor(Port.S1)

db = DriveBase(leftmotor,rightmotor,82,50)

#functions

def driveForward(speed,distanceInCm):
    GyroSensor.reset_angle(0,Direction.CLOCKWISE)
    time.reset()
    while(time.time()<(distanceInCm/(10*speed))):
        error = -14(0-gyro.angle())
        db.Drive(speed,error)


#code

driveForward(30,100)
