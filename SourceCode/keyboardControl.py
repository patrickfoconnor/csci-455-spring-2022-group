import tkinter as tk

win = tk.tk()
keys = KeyControl(win)

win.bind('<Up>', keys.arrow)
win.bind('<Left>', keys.arrow)
win.bind('<Down>', keys.arrow)
win.bind('<Right>', keys.arrow)
win.bind('<space>', keys.arrow)
win.bind('<z>', keys.waist)
win.bind('<c>', keys.waist)
win.bind('<w>', keys.head)
win.bind('<s>', keys.head)
win.bind('<a>', keys.head)
win.bind('<d>', keys.head)
win.mainloop()
keys = KeyControl(win)

