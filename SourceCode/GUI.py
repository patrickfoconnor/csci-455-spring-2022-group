import tkinter as tk

class MyTK():
    def __init__(self, win):
        self.instructions = []
        self.win = win
        self.win.geometry("800x480")
        self.leftfr = tk.Frame(win,width=60)
        self.leftfr.pack(side=tk.LEFT)
        self.leftfr['borderwidth'] = 2
        self.leftfr['relief'] = 'raised'
        self.midframe = tk.Frame(win)
        self.midframe.pack(side=tk.BOTTOM)
        self.turnimg = tk.PhotoImage(file="GUI/turn.png")
        self.headpanimg = tk.PhotoImage(file="GUI/headpan.png")
        self.headtiltimg = tk.PhotoImage(file="GUI/headtilt.png")
        self.motorsimg = tk.PhotoImage(file="GUI/motors.png")
        self.speechimg = tk.PhotoImage(file="GUI/speechinput.png")
        self.talkingimg = tk.PhotoImage(file="GUI/talking.png")
        self.waistimg = tk.PhotoImage(file="GUI/waistturn.png")
        self.emptyimg =tk.PhotoImage(file="GUI/empty.png")
        self.leftfr['borderwidth'] = 2
        self.leftfr['relief'] = 'raised'

    def createCanvas(self):
        self.myCan = tk.Canvas(self.win, bg="#333333", width="500", height="500")
        self.myCan.bind('<Motion>', self.motion)
        self.myCan.pack()

    def createLabel(self):
        lab = tk.Label(self.win, text="Hello Tkinter!")
        lab.pack()

    def createButtons(self):
        # command = fun
        tk.Button(self.leftfr, text='Motors',image=self.motorsimg,command=lambda m="motors": self.commands(m)).grid(column=0, row=0)
        tk.Button(self.leftfr, text='Turn', image=self.turnimg,command=lambda m="turn": self.commands(m)).grid(column=0, row=1)
        tk.Button(self.leftfr, text='Head Tilt',image=self.headtiltimg,command=lambda m="headtilt": self.commands(m)).grid(column=0, row=2)
        tk.Button(self.leftfr, text='Head Pan', image=self.headpanimg,command=lambda m="headpan": self.commands(m)).grid(column=0, row=3)
        tk.Button(self.leftfr, text='Waist Turn',image=self.waistimg,command=lambda m="waist": self.commands(m)).grid(column=0, row=4)
        tk.Button(self.leftfr, text='Speech Input',image=self.speechimg,command=lambda m="speech": self.commands(m)).grid(column=0, row=5)
        tk.Button(self.leftfr, text='Talking',image=self.talkingimg,command=lambda m="talking": self.commands(m)).grid(column=0, row=6)

        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=0, row=0)
        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=1, row=0)
        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=2, row=0)
        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=3, row=0)
        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=4, row=0)
        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=5, row=0)
        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=6, row=0)
        tk.Button(self.midframe, text="instruction1", image=self.emptyimg).grid(column=7, row=0)


    def createInstruction(self,name,args):
        temp = [name]
        for arg in args:
            temp.append(arg)
        self.instructions.append(temp)
        print("Created instruction ")
        print(temp)

    def parseSpeech(self):
        pass

    def motors(self,speed,time,direction):
        pass

    def turn(self,direction,seconds):
        print("Turn %s for %d seconds" % (direction,seconds))

    def headtilt(self,direction):
        print("Head tilt %s" % (direction))

    def headpan(self,direction):
        print("Head pan %s" % (direction))

    def waistturn(self,direction):
        print("Waist turn %s" % (direction))

    def speech(self):
        print("Say a command")
        command = ""
        #parse and call speech input hereee

    def talking(self,sentence):
        print("The robot says %s" % (sentence))
        #to do make robot speak

    def commands(self,name):
        top = tk.Toplevel(self.win)
        x = self.win.winfo_pointerx()
        y = self.win.winfo_pointery()
        top.geometry("%dx%d+%d+%d" %(200,150,x,y))
        top.title(name)
        fr = tk.Frame(top)
        fr.pack(fill='x',padx=5, pady=5)
        selected = tk.StringVar()
        args = []
        if name in "motors":
            pass
        elif name in "turn":
            label = tk.Label(fr, text="Direction to turn:")
            r1 = tk.Radiobutton(fr, text="Right", value="right", variable=selected, indicator = 0,background = "light blue")
            r2 = tk.Radiobutton(fr, text="Left", value="left", variable=selected,indicator = 0,background = "light blue")
            label.pack(fill='x', padx=5, pady=5)
            r1.pack(fill='x',padx=5, pady=5)
            r2.pack(fill='x',padx=5, pady=5)
            ok = tk.Button(fr, text="Ok", background="green",command=lambda: [args.append(selected.get()),self.createInstruction(name, args), top.destroy()])
            ok.pack(fill='x', padx=5, pady=5)
        elif name in "headtilt":
            label = tk.Label(fr, text="Direction to tilt head:")
            r1 = tk.Radiobutton(fr, text="Right", value="right", variable=selected, indicator=0,background="light blue")
            r2 = tk.Radiobutton(fr, text="Left", value="left", variable=selected, indicator=0, background="light blue")
            label.pack(fill='x', padx=5, pady=5)
            r1.pack(fill='x', padx=5, pady=5)
            r2.pack(fill='x', padx=5, pady=5)
            ok = tk.Button(fr, text="Ok", background="green", command=lambda: [args.append(selected.get()),self.createInstruction(name, args), top.destroy()])
            ok.pack(fill='x', padx=5, pady=5)
        elif name in "headpan":
            label = tk.Label(fr, text="Direction to pan head:")
            r1 = tk.Radiobutton(fr, text="Down", value="down", variable=selected, indicator=0,
                                background="light blue")
            r2 = tk.Radiobutton(fr, text="Up", value="up", variable=selected, indicator=0, background="light blue")
            label.pack(fill='x', padx=5, pady=5)
            r1.pack(fill='x', padx=5, pady=5)
            r2.pack(fill='x', padx=5, pady=5)
            ok = tk.Button(fr, text="Ok", background="green", command=lambda: [args.append(selected.get()), self.createInstruction(name, args),top.destroy()])
            ok.pack(fill='x', padx=5, pady=5)
        elif name in "waist":
            label = tk.Label(fr, text="Direction to spin waist:")
            r1 = tk.Radiobutton(fr, text="Right", value="right", variable=selected, indicator=0, background="light blue")
            r2 = tk.Radiobutton(fr, text="Left", value="left", variable=selected, indicator=0, background="light blue")
            label.pack(fill='x', padx=5, pady=5)
            r1.pack(fill='x', padx=5, pady=5)
            r2.pack(fill='x', padx=5, pady=5)
            ok = tk.Button(fr, text="Ok", background="green", command=lambda: [args.append(selected.get()), self.createInstruction(name, args),top.destroy()])
            ok.pack(fill='x', padx=5, pady=5)
        elif name in "speech":
            label = tk.Label(fr, text="Think of an instruction to")
            label2 = tk.Label(fr, text="say to the robot and press Ok")
            label.pack(fill='x', padx=5, pady=5)
            label2.pack(fill='x', padx=5, pady=5)
            ok = tk.Button(fr, text="Ok", background="green",command=lambda: [self.createInstruction(name, args),top.destroy()])
            ok.pack(fill='x', padx=5, pady=5)

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
win.configure(background='light blue')
v = MyTK(win)
##Key bindings
#win.bind('<Motion>', v.motion)
win.bind('<Right>', v.arrow)
win.bind('<Button>', v.mouseClick)

# create a canvas and add it to window
# v.createCanvas()
# Place a label on Window
#v.createLabel()
v.createButtons()
win.mainloop()
