from tkinter import *


# Methods for Moving the robot waist
class testRobot:
    def waistLeft(self):
        pass

    def waistRight(self):
        pass

    def headDown(self):
        pass

    def headUp(self):
        pass

    def headLeft(self):
        pass

    def headRight(self):
        pass

    def driveForward(self):
        pass

    def driveBackward(self):
        pass

    def turnLeft(self):
        pass

    def turnRight(self):
        pass


#       +-------------------+--------------------------------------------------+
#       |      Actions      |                                                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                 TimeLine Window                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                                                  |
#       |        BTN*       |                                                  |
#       +-------------------+--------------------------------------------------+
#       |    Insert BTN     |    Clear Timeline BTN     |    Start BTN         |
#       +-------------------+--------------------------------------------------+


root = Tk()  # Makes the window
root.wm_title("Operating Robot 30")  # Makes the title that will appear in the top left
root.config(background="#fff")  # sets background color to white

# put widgets here


# Left Frame and its contents
leftFrame = Frame(root, width=600, height=200)
# leftFrame.grid(row=1, column=1, padx=10, pady=2)

# Label(leftFrame, text="Actions:").grid(row=0, column=0, padx=10, pady=2)


l1 = Label(root, text='Actions', bg="#fff")
l1.grid(row=1, column=1)

# Instruct = Label(leftFrame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
# Instruct.grid(row=1, column=0, padx=10, pady=2)
# btnFrame = Frame(root, width=200, height=200)
# btnFrame.grid(row=3, column=1, padx=10, pady=2)

# actionLog = Text(leftFrame, width=30, height=10, takefocus=0)
# actionLog.grid(row=2, column=0, padx=10, pady=2)

# Need 10 button for:
#  1) Drive Option 01: Motor sent speed, time, direction
#  2) Drive Option 02: Robot turn left right for x seconds
#  3) Head Tilt Up
#  4) Head Tilt Down
#  5) Head Pan Left
#  6) Head Pan Right
#  7) Waist Left
#  8) Waist Right
#  9) Speech Input
# 10) Text to speech

allButtons = []

drivingOneBtn = Button(
    text="Drive Option 1",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(drivingOneBtn)

drivingTwoBtn = Button(
    text="Drive Option 2",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(drivingTwoBtn)

headUpBtn = Button(
    text="Head Tilt Up",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(headUpBtn)

headDownBtn = Button(
    text="Head Tilt Down",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(headDownBtn)

headLeftBtn = Button(
    text="Head Pan Left",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(headLeftBtn)

headRightBtn = Button(
    text="Head Pan Right",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(headRightBtn)

waistLeftBtn = Button(
    text="Waist Left",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(waistLeftBtn)

waistRightBtn = Button(
    text="Waist Right",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(waistRightBtn)

speechToInputBtn = Button(
    text="Speech to Input",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(speechToInputBtn)

textToSpeechBtn = Button(
    text="Text to Speech",
    height=2,
    width=20,
    bd="5",
    bg="blue",
    command=driveBackward()
)
allButtons.append(textToSpeechBtn)

drivingOneBtn = Button(
    # image = ImageTk.PhotoImage(Image.open("../guiIcons/test.png")),
    text="Insert",
    # compound="top",
    height=4,
    width=20,
    bd="5",
    bg="yellow",
    command=driveBackward()
)
allButtons.append(drivingOneBtn)

for index in range(0, len(allButtons)):
    row = index + 3
    allButtons[index].grid(row=row, column=0, padx=10, pady=2)
    print(row)

l2 = Label(root, text=' row=1,column=2')
l2.grid(row=1, column=2)
# Right Frame and its contents
timelineFrame = Frame(root, width=200, height=600, bg="white")
timelineFrame.grid(
    row=1,
    column=2,
    padx=10,
    pady=2,
    rowspan="13",
    colspan="3",
)

drivingOneBtn = Button(
    text="Clear Timeline",
    height=4,
    width=20,
    bd="5",
    bg="Red",
    command=driveBackward()
)

root.mainloop()  # start monitoring and updating the GUI. Nothing below here runs.
