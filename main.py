from tkinter import *
from battleShip import *
from tkinter import messagebox

window = None

def option():
    global window
    value = var.get()

    if not value:
        messagebox.showwarning("Warning", "Choose an options")
        return

    if window:
        window.destroy()

    if var.get() == 1:
        window = SinglePlayerBattleShip()
    else:
        window = BattleShip()
    

root = Tk()
root.title("Main Menu")
root.geometry("500x200")

frame = Frame(root)
frame.pack()

labelFrame = LabelFrame(frame, text="Options")
labelFrame.pack()

label = Label(labelFrame, text="Game Mode")
label.grid(column=1, row=0)

var = IntVar()

radio_button_1 = Radiobutton(labelFrame, text="Player vs Computer", variable=var, value=1)
radio_button_1.grid(column=0, row=1)

radio_button_2 = Radiobutton(labelFrame, text="Player vs Player", variable=var, value=2)
radio_button_2.grid(column=2, row=1)

button = Button(labelFrame, text="PLAY!!", command=option)
button.grid(column=1, row=2)

root.mainloop()