# Main class that will hold base Robot object

# TODO
# Get the wheels moving forward
# Get the wheels moving backwards
# Turn Right
# Turn Left
# Redo movements to incorporate for loop to reduce jerk

from enum import Enum
import serial
import sys
import time

# SERVO CONSTANTS
TARGET_CENTER = 5896
MAX_SERVO = 7500
MIN_SERVO = 4500
SERVO_INCREMENT = 1000
INCREMENT = 10

# MOTOR CONSTANTS
MOTOR_SPEED = 6001
MOTOR_INCREMENT = 500
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
    speed = MOTOR_SPEED

    # constructor
    def __init__(self):
        self.usb = getUSB()
        self.resetRobot()

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

    # Methods for Moving the robot waist
    def waistLeft(self):
        counter = 0
        while (counter <= SERVO_INCREMENT):
            self.motors -= INCREMENT
            if (self.motors > MAX_SERVO):
                self.motors = MAX_SERVO
            self.writeCmd(RobotMotor.Waist, self.motors)
            counter += INCREMENT

    def waistRight(self):
        counter = 0
        while (counter <= SERVO_INCREMENT):
            self.motors += INCREMENT
            if (self.motors < MIN_SERVO):
                self.motors = MIN_SERVO
            self.writeCmd(RobotMotor.Waist, self.motors)
            counter += INCREMENT

    # Methods for Moving the robot head
    def headUp(self):
        counter = 0
        while (counter <= SERVO_INCREMENT):
            self.motors += INCREMENT
            if (self.motors > MAX_SERVO):
                self.motors = MAX_SERVO
            self.writeCmd(RobotMotor.HeadY, self.motors)
            counter += INCREMENT

    def headDown(self):
        counter = 0
        while (counter <= SERVO_INCREMENT):
            self.motors -= INCREMENT
            if (self.motors < MIN_SERVO):
                self.motors = MIN_SERVO
            self.writeCmd(RobotMotor.HeadY, self.motors)
            counter += INCREMENT

    def headLeft(self):
        counter = 0
        while (counter <= SERVO_INCREMENT):
            self.motors += INCREMENT
            if (self.motors > MAX_SERVO):
                self.motors = MAX_SERVO
            self.writeCmd(RobotMotor.HeadX, self.motors)
            counter += INCREMENT

    def headRight(self):
        counter = 0
        while (counter <= SERVO_INCREMENT):
            self.motors -= INCREMENT
            if (self.motors < MIN_SERVO):
                self.motors = MIN_SERVO
            self.writeCmd(RobotMotor.HeadX, self.motors)
            counter += INCREMENT

    # Methods for driving the robot
    def driveForward(self):
        #self.resetMotor(self.motors)
        self.speed += MOTOR_INCREMENT
        if (self.speed > MAX_SERVO):
            self.sspeed = MAX_SERVO
        self.writeCmd(RobotMotor.WheelLeft, self.speed)
        self.writeCmd(RobotMotor.WheelRight, self.speed)

    def driveBackward(self):
        pass

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def resetMotor(self, motor):
        if (self.motors > 6000):
            self.motors = self.motors
        else:
            self.motors = 6000

    def resetRobot(self):
        for motor in RobotMotor:
            self.writeCmd(motor, TARGET_CENTER)
        # center robot waist
        # self.writeCmd(RobotMotor.Waist, TARGET_CENTER)
        # center robot head on X
        # self.writeCmd(RobotMotor.HeadX, TARGET_CENTER)
        # center robot head on Y
        # self.writeCmd(RobotMotor.HeadY, TARGET_CENTER)

    def killRobot(self):
        self.win.destroy()


robot = TangoRobot()
