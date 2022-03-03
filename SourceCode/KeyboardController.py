

from SourceCode.TangoRobot import *


def arrows(self, event):
    keycode = event.keycode
    if keycode == 111:
        print("Up Arrow")
        self.resetMotor(RobotMotor.WheelLeft)
        self.motors += MOTOR_INCREMENT
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


robot = TangoRobot()
