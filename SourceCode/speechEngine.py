from TangoRobot import *


class SpeechEngine:
    def __init__(self, command):
        self.command = command

    def arrows(self):
        if "forward" in self.command:
            print("Forward")
            time.sleep(.2)
            robot.driveForward()
        elif "back" in self.command:
            print("Backward")
            time.sleep(.2)
            robot.driveBackward()
        elif "left" in self.command:
            print("Left")
            time.sleep(.2)
            robot.turnLeft()
        elif "right" in self.command:
            print("Right")
            time.sleep(.2)
            robot.turnRight()

    def waist(self):
        if "left" in self.command:
            print("Bend Left")
            time.sleep(.2)
            robot.waistLeft()
        elif "right" in self.command:
            print("Bend Right")
            time.sleep(.2)
            robot.waistRight()

    def head(self):
        if "up" in self.command:
            print("Head Up")
            time.sleep(.2)
            robot.headUp()
        elif "down" in self.command:
            print("Head Down")
            time.sleep(.2)
            robot.headDown()
        elif "left" in self.command:
            print("Head Left")
            time.sleep(.2)
            robot.headLeft()
        elif "right" in self.command:
            print("Head Right")
            time.sleep(.2)
            robot.headRight()

    def stop(self):
        print("Halting")
        robot.resetRobot()
