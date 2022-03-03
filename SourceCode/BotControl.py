# Controls
#

import serial
import sys
import time
from enum import Enum
import tkinter as tk

TARGET_CENTER = 6000
MAX_SERVO = 8000
MIN_SERVO = 4000
SERVO_INCREMENT = 100

MOTOR_TARGET_RESET = 6001  # 6000


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
    WheelLeft = 0x00
    WheelRight = 0x01
    Waist = 0x02
    HeadX = 0x03
    HeadY = 0x04
    ArmLeft = 0x05
    ArmRight = 0x06


class TangoRobot:
    # class properties
    usb = None
    win = None
    motors = 0

    # constructor
    def __init__(self):
        self.usb = getUSB()
        # center robot waist
        self.writeCmd(RobotMotor.Waist, TARGET_CENTER)
        # center robot head on X
        self.writeCmd(RobotMotor.HeadX, TARGET_CENTER)
        # center robot head on Y
        self.writeCmd(RobotMotor.HeadY, TARGET_CENTER)
        # tkinter window
        self.win = tk.Tk()
        # setup keybindings
        self.win.bind('<Up>', self.arrows)  # key code: 111
        self.win.bind('<Down>', self.arrows)  # key code: 116
        self.win.bind('<Left>', self.arrows)  # key code: 113
        self.win.bind('<Right>', self.arrows)  # key code: 114
        self.win.bind('<space>', self.stop)  # key code: 65
        self.win.bind('<w>', self.head)  # key code: 25
        self.win.bind('<s>', self.head)  # key code: 39
        self.win.bind('<a>', self.head)  # key code: 38
        self.win.bind('<d>', self.head)  # key code: 40
        self.win.bind('<z>', self.waist)  # key code: 52
        self.win.bind('<c>', self.waist)  # key code: 54
        # start tkinter window
        self.win.mainloop()

    # write out command to usb
    def writeCmd(self, motor, target):
        # Validate that 'motor' is of type 'RobotMotor' enum class
        if not isinstance(motor, RobotMotor):
            # Show error, motor is not of correct type
            print("Motor must be type {!s} - type '{!s}' not accepted".format(type(RobotMotor), type(motor)))
            return
        # Build command
        lsb = target & 0x7F
        msb = (target >> 7) & 0x7F
        command = chr(0xaa) + chr(0xC) + chr(0x04) + chr(motor.value) + chr(lsb) + chr(msb)
        # Check if usb is not None
        if self.usb is not None:
            # Write out command
            self.usb.write(command.encode('utf-8'))

    def arrows(self, event):
        keycode = event.keycode
        if keycode == 111:
            print("Up Arrow")
            self.resetMotor()
            self.motors -= SERVO_INCREMENT
            if (self.motors > MAX_SERVO):
                self.motors = MAX_SERVO
            self.writeCmd(RobotMotor.WheelLeft, self.motors)
        elif keycode == 116:
            print("Down Arrow")
        elif keycode == 113:
            print("Left Arrow")
        elif keycode == 114:
            print("Right Arrow")


    def waist(self, event):
        keycode = event.keycode
        if keycode == 52:
            print("Z (Left)")
            self.waistLeft()

        elif keycode == 54:
            print("C (Right)")
            self.waistRight()


    def head(self, event):
        keycode = event.keycode
        if keycode == 25:
            print("W: Head Up")
            self.headUp()

        elif keycode == 39:
            print("S: Head Down")
            self.headDown()

        elif keycode == 38:
            print("A: Head Left")
            self.headLeft()
        elif keycode == 40:
            print("D: Head Right")
            self.headRight()

    def stop(self, event=None):
        self.win.destroy()

    def waistLeft(self):
        self.motors -= SERVO_INCREMENT
        if (self.motors > MAX_SERVO):
            self.motors = MAX_SERVO
        self.writeCmd(RobotMotor.Waist, self.motors)

    def waistRight(self):
        self.motors += SERVO_INCREMENT
        if (self.motors < MIN_SERVO):
            self.motors = MIN_SERVO
        self.writeCmd(RobotMotor.Waist, self.motors)

    def headUp(self):
        self.motors += SERVO_INCREMENT
        if (self.motors > MAX_SERVO):
            self.motors = MAX_SERVO
        self.writeCmd(RobotMotor.HeadY, self.motors)

    def headDown(self):
        self.motors -= SERVO_INCREMENT
        if (self.motors < MIN_SERVO):
            self.motors = MIN_SERVO
        self.writeCmd(RobotMotor.HeadY, self.motors)

    def headLeft(self):
        self.motors += SERVO_INCREMENT
        if (self.motors > MAX_SERVO):
            self.motors = MAX_SERVO
        self.writeCmd(RobotMotor.HeadX, self.motors)

    def headRight(self):
        self.motors -= SERVO_INCREMENT
        if (self.motors < MIN_SERVO):
            self.motors = MIN_SERVO
        self.writeCmd(RobotMotor.HeadX, self.motors)


robot = TangoRobot()
