import tkinter as tk
from PIL import Image, ImageTk

class MyTK():
    def __init__(self, win):
        self.win = win
        self.win.geometry("800x480")
        self.leftfr = tk.Frame(win)
        self.leftfr.columnconfigure(0,weight=1)
        self.leftfr.pack(side=tk.LEFT)
        self.rightfr = tk.Frame(win)
        self.rightfr.pack(side=tk.RIGHT)
        self.rightfr.columnconfigure(1,weight=0)
        self.turnimg = tk.PhotoImage(file="GUI/turn.png")
        self.headpanimg = tk.PhotoImage(file="GUI/headpan.png")
        self.headtiltimg = tk.PhotoImage(file="GUI/headtilt.png")
        self.motorsimg = tk.PhotoImage(file="GUI/motors.png")
        self.speechimg = tk.PhotoImage(file="GUI/speechinput.png")
        self.talkingimg = tk.PhotoImage(file="GUI/talking.png")
        self.waistimg = tk.PhotoImage(file="GUI/waistturn.png")
        self.leftfr['borderwidth'] = 2
        self.leftfr['relief'] = 'raised'
        # width = self.win.winfo_screenwidth()
        # height = self.win.winfo_screenheight()
        # self.win.geometry("%dx%d"%(width, height))

    def createCanvas(self):
        self.myCan = tk.Canvas(self.win, bg="#333333", width="500", height="500")
        self.myCan.bind('<Motion>', self.motion)
        self.myCan.pack()

    def createLabel(self):
        lab = tk.Label(self.win, text="Hello Tkinter!")
        lab.pack()

    def createButton(self):
        # command = fun
        tk.Button(self.leftfr, text='Motors',image=self.motorsimg).grid(column=0, row=0)
        tk.Button(self.leftfr, text='Turn', image=self.turnimg).grid(column=0, row=1)
        tk.Button(self.leftfr, text='Head Tilt',image=self.headtiltimg).grid(column=0, row=2)
        tk.Button(self.leftfr, text='Head Pan', image=self.headpanimg).grid(column=0, row=3)
        tk.Button(self.leftfr, text='Waist Turn',image=self.waistimg).grid(column=0, row=4)
        tk.Button(self.leftfr, text='Speech Input',image=self.speechimg).grid(column=0, row=5)
        tk.Button(self.leftfr, text='Talking',image=self.talkingimg).grid(column=0, row=6)
        # button = tk.Button(self.leftfr, width="45", text="print", bg="blue", fg="yellow",
        #                    command=lambda m="#print button pressed": self.fun3(m))
        # button.pack(side=tk.TOP)
        # button2 = tk.Button(self.leftfr, width="15", text="Second", bg="blue", fg="yellow",
        #                     command=lambda m="#second button pressed": self.fun3(m))
        # button2.pack(side=tk.LEFT)
        # button2 = tk.Button(self.leftfr, width="15", text="exit", bg="blue", fg="yellow",
        #                     command=lambda m="exit": self.fun3(m))
        # button2.pack(side=tk.BOTTOM)
    def motors(self,speed,time,direction):
        pass

    def turn(self,direction,seconds):
        pass

    def headtitlt(self,direction):
        pass

    def headpan(self,direction):
        pass

    def waistturn(self,direction):
        pass

    def speech(self,direction):
        pass

    def talking(self,sentence):
        pass

    def fun(self):
        print("Print is pushed")

    def fun2(self):
        print("Second is pressed")

    def fun3(self, name):
        print(name)
        if (name == "exit"):
            print("leaving")
            self.win.destroy()

    def motion(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        return

    def mouseClick(self, event):
        print(event)

    def arrow(self, key):
        # print("Arrow up")
        print(self, key)
        if key.keycode == 39:
            print("Right")


win = tk.Tk()
win.configure(background='#121212')
v = MyTK(win)
##Key bindings
win.bind('<Up>', v.arrow)
win.bind('<Right>', v.arrow)
win.bind('<Button>', v.mouseClick)

# create a canvas and add it to window
# v.createCanvas()
# Place a label on Window
#v.createLabel()
v.createButton()
win.mainloop()
