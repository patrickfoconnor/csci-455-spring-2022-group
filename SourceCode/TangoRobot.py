# Main class that will hold base Robot object

from enum import Enum
import serial
import sys
import time

# SERVO CONSTANTS
TARGET_CENTER = 6000
MAX_SERVO = 7600
MIN_SERVO = 4400
SERVO_INCREMENT = 225
SERVO_INCREMENT_WAIST = 750
INCREMENT = 10

# MOTOR CONSTANTS

MOTOR_SPEED = 6000

MOTOR_INCREMENT = 200
MOTOR_TARGET_RESET = 6000  # 6000


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
    Forward = 0x01
    Turn = 0x02
    Waist = 0x00
    HeadX = 0x03
    HeadY = 0x04
    ArmLeft = 0x05
    ArmRight = 0x06


class TangoRobot:
    # class properties
    usb = None
    win = None
    motors = 0
    driveSpeed = MOTOR_SPEED
    dummy = False

    # constructor
    def __init__(self):
        self.usb = getUSB()
        self.resetRobot()
        self.driveSpeed = 6000
        self.turn = 6000

    # write out command to usb
    '''
    def setTarget(self, motor, target):
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
    '''
    def sendCmd(self, cmd):
        cmdStr = chr(0xaa) + chr(0x0c) + cmd
        self.usb.write(bytes(cmdStr, 'latin-1'))

    def setTarget(self, chan, target):
        if not isinstance(chan, RobotMotor):
            # Show error, motor is not of correct type
            print("Motor must be type {!s} - type '{!s}' not accepted".format(type(RobotMotor), type(motor)))
            return

        lsb = target & 0x7f  # 7 bits for least significant byte
        msb = (target >> 7) & 0x7f  # shift 7 and take next 7 bits for msb
        cmd = chr(0x04) + chr(chan.value) + chr(lsb) + chr(msb)
        self.sendCmd(cmd)

    # Methods for Moving the robot waist
    def waistLeft(self):
        counter = 0
        while (counter <= SERVO_INCREMENT_WAIST):
            self.motors -= INCREMENT
            if (self.motors > MAX_SERVO):
                self.motors = MAX_SERVO
            self.setTarget(RobotMotor.Waist, self.motors)
            counter += INCREMENT

    def waistRight(self):
        counter = 0
        while counter <= SERVO_INCREMENT_WAIST:
            self.motors += INCREMENT
            if self.motors < MIN_SERVO:
                self.motors = MIN_SERVO
            self.setTarget(RobotMotor.Waist, self.motors)
            counter += INCREMENT

    # Methods for Moving the robot head
    def headUp(self):
        counter = 0
        while counter <= SERVO_INCREMENT:
            self.motors += INCREMENT
            if self.motors > MAX_SERVO:
                self.motors = MAX_SERVO
            self.setTarget(RobotMotor.HeadY, self.motors)
            counter += INCREMENT

    def headDown(self):
        counter = 0
        while counter <= SERVO_INCREMENT:
            self.motors -= INCREMENT
            if (self.motors < MIN_SERVO):
                self.motors = MIN_SERVO
            self.setTarget(RobotMotor.HeadY, self.motors)
            counter += INCREMENT

    def headLeft(self):
        counter = 0
        while counter <= SERVO_INCREMENT:
            self.motors += INCREMENT
            if self.motors > MAX_SERVO:
                self.motors = MAX_SERVO
            self.setTarget(RobotMotor.HeadX, self.motors)
            counter += INCREMENT

    def headRight(self):
        counter = 0
        while counter <= SERVO_INCREMENT:
            self.motors -= INCREMENT
            if self.motors < MIN_SERVO:
                self.motors = MIN_SERVO
            self.setTarget(RobotMotor.HeadX, self.motors)
            counter += INCREMENT

    # Methods for driving the robot
    def driveForward(self):
        if self.driveSpeed > 6400:
            self.driveSpeed == 6400
        self.driveSpeed -= MOTOR_INCREMENT
        if self.driveSpeed < MIN_SERVO:
            self.driveSpeed = MIN_SERVO
            print("Too Speedy")
        self.setTarget(RobotMotor.Forward, self.driveSpeed)
        print(self.driveSpeed)

    def driveBackward(self):
        if self.driveSpeed > 6400:
            self.driveSpeed == 6400
        self.driveSpeed += MOTOR_INCREMENT
        if self.driveSpeed > MAX_SERVO:
            self.driveSpeed = MAX_SERVO
            print("Too Slow")
        self.setTarget(RobotMotor.Forward, self.driveSpeed)
        # self.setTarget(RobotMotor.Turn, self.driveSpeed)
        print(self.driveSpeed)

    def turnLeft(self):
        if self.driveSpeed > 6400:
            self.driveSpeed == 6400
        self.turn += 200  # MOTOR_INCREMENT
        if self.turn > MAX_SERVO:
            self.turn = MAX_SERVO
        self.setTarget(RobotMotor.Turn, self.turn)
        print(self.turn)

    def turnRight(self):
        if self.driveSpeed > 6400:
            self.driveSpeed == 6400
        self.turn -= 200  # MOTOR_INCREMENT
        if self.turn < MIN_SERVO:
            self.turn = MIN_SERVO
        self.setTarget(RobotMotor.Turn, self.turn)
        print(self.turn)

    def resetRobot(self):
        # Center all motors to 6000
        for motor in RobotMotor:
            self.setTarget(motor, TARGET_CENTER)
            time.sleep(.5)

    def resetWheels(self):
        # Center all robot motors to 6000
        self.setTarget(RobotMotor.Turn, TARGET_CENTER)
        self.setTarget(RobotMotor.Forward, TARGET_CENTER)



robot = TangoRobot()
