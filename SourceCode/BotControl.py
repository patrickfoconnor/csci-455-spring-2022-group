import serial
import sys
import time
from enum import Enum
import tkinter as tk

TARGET_CENTER = 5896

def getUSB():
    usb = None
    try:
        usb = serial.Serial('/dev/ttyACM0')
        print(usb.name)
        print(usb.baudrate)
    except:
        try:
            usb = serial.Serial('/dev/ttyACM1')
            print(usb.name)
            print(usb.baudrate)
        except:
            print("No servo serial ports found")
            sys.exit(0)
    return usb

class RobotMotor(Enum):
    WheelLeft=0x00
    WheelRight=0x01
    Waist=0x02
    HeadX=0x03
    HeadY=0x04
    ArmLeft=0x05
    ArmRight=0x06

class TangoRobot:

    # class properties
    usb = None
    win = None

    # constructor
    def __init__(self):
        self.usb = getUSB()
        # center robot waist
        self.writeCmd(RobotMotor.Waist, TARGET_CENTER)
        # tkinter window
        self.win = tk.Tk()
        # setup keybindings
        self.win.bind('<Up>', self.arrows)   # key code: 111
        self.win.bind('<Down>', self.arrows) # key code: 116
        self.win.bind('<Left>', self.arrows) # key code: 113
        self.win.bind('<Right>', self.arrows) # key code: 114
        self.win.bind('<space>', self.stop) # key code: 65
        self.win.bind('<w>', self.head) # key code: 25
        self.win.bind('<s>', self.head) # key code: 39
        self.win.bind('<a>', self.head) # key code: 38
        self.win.bind('<d>', self.head) # key code: 40
        self.win.bind('<z>', self.waist) # key code: 52
        self.win.bind('<c>', self.waist) # key code: 54
        # start tkinter window
        self.win.mainloop()

    # write out command to usb
    def writeCmd(self, motor, target=TARGET_CENTER):
        # Validate that 'motor' is of type 'RobotMotor' enum class
        if not isinstance(motor, RobotMotor):
            # Show error, motor is not of correct type
            print("Motor must be type {!s} - type '{!s}' not accepted".format(type(RobotMotor), type(motor)))
            return
        # Build command
        lsb = target &0x7F
        msb = (target >> 7) & 0x7F
        command = chr(0xaa) + chr(0xC) + chr(0x04) + chr(motor.value) + chr(lsb) + chr(msb)
        # Check if usb is not None
        if self.usb is not None:
            # Write out command
            self.usb.write(command.encode('utf-8'))
