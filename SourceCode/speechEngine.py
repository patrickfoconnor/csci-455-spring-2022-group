from TangoRobot import *


class SpeechEngine:

    def arrows(command):
        if "forward" in command:
            print("Forward")
            time.sleep(.2)
            robot.driveForward()
        elif "back" in command:
            print("Backward")
            time.sleep(.2)
            robot.driveBackward()
        elif "left" in command:
            print("Left")
            time.sleep(.2)
            robot.turnLeft()
        elif "right" in command:
            print("Right")
            time.sleep(.2)
            robot.turnRight()

    def waist(command):
        if "left" in command:
            print("Bend Left")
            time.sleep(.2)
            robot.waistLeft()
        elif "right" in command:
            print("Bend Right")
            time.sleep(.2)
            robot.waistRight()

    def head(command):
        if "up" in command:
            print("Head Up")
            time.sleep(.2)
            robot.headUp()
        elif "down" in command:
            print("Head Down")
            time.sleep(.2)
            robot.headDown()
        elif "left" in command:
            print("Head Left")
            time.sleep(.2)
            robot.headLeft()
        elif "right" in command:
            print("Head Right")
            time.sleep(.2)
            robot.headRight()

    def stop(self):
        print("Halting")
        robot.resetRobot()
