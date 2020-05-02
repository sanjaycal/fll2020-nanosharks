from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Drive ():
    def __init__(self,leftMotor,rightMotor,gyroport):
        lm = leftMotor
        rm = rightMotor
        db = DriveBase(lm,rm,82,50)
        gy = GyroSensor(gyroport)
    def forward(self,distance,speed):
        db.drive(speed,0)
        wait(distance/(10*speed))

    def PID(self,P,I,D,bias,iterationTime,speed):
        gyro = GyroSensor(Port.S1)
        error_prior = 0
        integral = 0
        lm = Motor(Port.B)
        rm = Motor(Port.C)
        db = DriveBase(lm,rm,82,50)
        while (True):
            error = 0-gyro.angle()
            integral = integral+(error*iterationTime) 
            derivative = (error-error_prior)/iterationTime
            output = P*error+I*integral+D*derivative+bias
            error_prior = error
            db.drive(speed,output)
            print(error)
            wait(iterationTime)

