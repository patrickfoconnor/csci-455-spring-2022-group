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
        tk.Button(self.leftfr, text='Motors',image=self.motorsimg,command=lambda m="motors": self.commands(m)).grid(column=0, row=0)
        tk.Button(self.leftfr, text='Turn', image=self.turnimg,command=lambda m="turn": self.commands(m)).grid(column=0, row=1)
        tk.Button(self.leftfr, text='Head Tilt',image=self.headtiltimg,command=lambda m="headtilt": self.commands(m)).grid(column=0, row=2)
        tk.Button(self.leftfr, text='Head Pan', image=self.headpanimg,command=lambda m="headpan": self.commands(m)).grid(column=0, row=3)
        tk.Button(self.leftfr, text='Waist Turn',image=self.waistimg,command=lambda m="waist": self.commands(m)).grid(column=0, row=4)
        tk.Button(self.leftfr, text='Speech Input',image=self.speechimg,command=lambda m="speech": self.commands(m)).grid(column=0, row=5)
        tk.Button(self.leftfr, text='Talking',image=self.talkingimg,command=lambda m="talking": self.commands(m)).grid(column=0, row=6)




    def motors(self,speed,time,direction):
        pass

    def turn(self,direction,seconds):
        print("Turn %s %d" % (direction,seconds))

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

    def commands(self,name):
        top = tk.Toplevel(self.win)
        x = self.win.winfo_pointerx()
        y = self.win.winfo_pointery()
        top.geometry("%dx%d+%d+%d" %(200,150,x,y))
        top.title(name)
        fr = tk.Frame(top)
        fr.pack(fill='x',padx=5, pady=5)
        selected = tk.StringVar()
        if name in "motors":
            pass
            b = tk.Button(fr, text="OK", width=10)
            b.pack()
        elif name in "turn":
            label = tk.Label(fr, text="Select a direction:")
            r1 = tk.Radiobutton(fr, text="Right", value="right", variable=selected, indicator = 0,background = "light blue")
            r2 = tk.Radiobutton(fr, text="Left", value="left", variable=selected,indicator = 0,background = "light blue")
            label.pack(fill='x', padx=5, pady=5)
            r1.pack(fill='x',padx=5, pady=5)
            r2.pack(fill='x',padx=5, pady=5)
            ok = tk.Button(fr, text="Ok", background="green",command=lambda: [self.turn(selected.get(), 100), top.destroy()])
            ok.pack(fill='x', padx=5, pady=5)
        elif name in "headtilt":
            pass
        elif name in "headpan":
            pass
        elif name in "waist":
            pass
        elif name in "speech":
            pass
        elif name in "talking":
            pass

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
win.title("Robot Program GUI")
win.configure(background='#121212')
v = MyTK(win)
##Key bindings
#win.bind('<Motion>', v.motion)
win.bind('<Right>', v.arrow)
win.bind('<Button>', v.mouseClick)

# create a canvas and add it to window
# v.createCanvas()
# Place a label on Window
#v.createLabel()
v.createButton()
win.mainloop()
