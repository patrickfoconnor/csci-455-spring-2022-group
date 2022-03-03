from TangoRobot import *


class KeyboardController:
    def __init__(self):
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

