import serial
import time

directon = 1

ser = serial.Serial("/dev/ttyACM0",9600,timeout=1)

def driveMotor(int speed, int drct):
    enA = speed

    # determine direction
    if drct == 1:
        in1 = 1
        in2 = 0
    else if drct == -1:
        in1 = 0
        in2 = 1
    else:
        in1 = 0
        in2 = 0
    
    valList = str(enA) + ',' + str(in1) + ',' + str(in2)
    serString = ','.join(valList)
    ser.write(serString)
    time.sleep(0.1)

while 1:
    # ramp up speed
    while motSpeed < 256:
        driveMotor(motSpeed, direction)
        motSpeed = motSpeed + 1
        

    # ramp down speed
    while motSpeed > 0:
        driveMotor(motSpeed, direction)
        motSpeed = motSpeed - 1

    # reverse direction
    direction = -direction

    
        
        
