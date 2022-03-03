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
            robot.resetMotor(RobotMotor.WheelLeft)
            robot.motors += MOTOR_INCREMENT
            if (robot.motors > MAX_SERVO):
                robot.motors = MAX_SERVO
            robot.writeCmd(RobotMotor.WheelLeft, robot.motors)
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
            robot.waistLeft()

        elif keycode == 54:
            print("C (Right)")
            robot.waistRight()

    def head(self, event):
        keycode = event.keycode
        if keycode == 25:
            print("W: Head Up")
            robot.headUp()

        elif keycode == 39:
            print("S: Head Down")
            robot.headDown()

        elif keycode == 38:
            print("A: Head Left")
            robot.headLeft()
        elif keycode == 40:
            print("D: Head Right")
            robot.headRight()

    def stop(self, event=None):
        robot.win.destroy()


keyboard = KeyboardController()
