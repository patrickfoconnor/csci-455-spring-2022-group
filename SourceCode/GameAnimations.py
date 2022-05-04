import tkinter as tk
import time

class GameAnimations:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Adventure Game")
        self.win.configure(background='light blue')
        self.win.geometry("700x480")
        self.fr = tk.Frame(self.win)
        self.fr.pack(side=tk.LEFT)
        self.canvas = tk.Canvas(self.win, highlightthickness=0, bg="light blue", width=480, height=480)
        self.canvas.pack()

    def Victory(self):
        txt = self.canvas.create_text((240,240),fill ="yellow", text="VICTORY ACHIEVED",font=("Times New Roman", 4))
        self.canvas.pack()
        self.win.update()
        for i in range(30):
            self.win.after(10)
            self.canvas.itemconfig(txt, font=("Times New Roman", 4 + (i)))
            self.canvas.pack()
            self.win.update()
        self.canvas.itemconfig(txt, font=("Times New Roman", 34))
        self.canvas.pack()
        self.win.update()
        self.win.after(3000,self.canvas.delete('all'))
        self.canvas.pack()
        self.win.update()

    def recharge(self):
        h0 = tk.PhotoImage(file="Game/heart0.png")
        h1 = tk.PhotoImage(file="Game/heart.png")
        h2 = tk.PhotoImage(file="Game/heart2.png")
        h3 = tk.PhotoImage(file="Game/heart3.png")
        h4 = tk.PhotoImage(file="Game/heart4.png")
        h5 = tk.PhotoImage(file="Game/heart5.png")
    def createButtons(self):
        B = tk.Button(self.fr, text="test", command=lambda: self.recharge())
        B.pack()



ani = GameAnimations()
ani.createButtons()
ani.win.mainloop()



