from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("200x300")


# Change the label text
def show():
    for i in range(0, 8):
        clicked = StringVar()

        # initial menu text
        clicked.set("Option {}".format(i + 1))

        # Create Dropdown menu
        drop = OptionMenu(root, clicked, *options)
        drop.pack(side=RIGHT)

        buttonValues.append(clicked)

    for i in (range(0,len(buttonValues))):
        print(buttonValues[i].get())

button = Button(root, text="click Me", command=show).pack(side=BOTTOM)
# Dropdown menu options
options = [
    "Move",
    "Turn",
    "Nod",
    "Shake",
    "Bend",
    "Listen",
    "Speak"
]

buttonValues = []

for i in range(0,8):
    clicked = StringVar()

    # initial menu text
    clicked.set("Option {}".format(i+1))

    # Create Dropdown menu
    drop = OptionMenu(root, clicked, *options)
    drop.pack(side=TOP)

    buttonValues.append(clicked)

# Create button, it will change label text


# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()