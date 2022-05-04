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
        self.createButtons()
        self.hearts = []
        self.hearts.append(tk.PhotoImage(file="Game/heart0.png"))
        self.hearts.append(tk.PhotoImage(file="Game/heart.png"))
        self.hearts.append(tk.PhotoImage(file="Game/heart2.png"))
        self.hearts.append(tk.PhotoImage(file="Game/heart3.png"))
        self.hearts.append(tk.PhotoImage(file="Game/heart4.png"))
        self.hearts.append(tk.PhotoImage(file="Game/heart5.png"))
        self.win.update_idletasks()
        self.win.update()

    def victory(self):
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
        for img in self.hearts:
            self.canvas.create_image((100,250),image=img,anchor=tk.W)
            self.canvas.pack()
            self.win.update()
            self.win.after(750)
        self.win.after(3000, self.canvas.delete('all'))
        self.canvas.pack()
        self.win.update()

    def createButtons(self):
        B = tk.Button(self.fr, text="test", command=lambda: self.recharge())
        B.pack()



ani = GameAnimations()



