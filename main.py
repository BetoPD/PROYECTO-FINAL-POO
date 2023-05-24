from tkinter import *
from battleShipSinglePlayer import *
import PyInstaller
# from multiplayerBattleShip import *

pathGift = Image.open("mike-o-hearn.gif")
window = None

def option():
    global window
    value = var.get()
 
    if not value:
        messagebox.showwarning("Hey dude!!!", "Hey Dude!!!\nChoose an option")
        return

    if window:
        window.destroy()

    pygame.mixer.music.pause()

    if var.get() == 1:
        window = SinglePlayerBattleShip()
    else:
        messagebox.showwarning("Hey dude!!!", "Hey Dude!!!\nChoose an option")
        # window = MultiPlayerBattleShip()
    

root = Tk()
root.title("Main Menu")
root.geometry("600x600")
root.iconbitmap("pb.ico")
pygame.mixer.init()
play()

###

# Create a list to store each frame of the GIF

frames = []

# Extract each frame from the GIF

try:
    while True:
        frames.append(ImageTk.PhotoImage(pathGift))
        pathGift.seek(pathGift.tell() + 1)
except EOFError:
    pass

###


frame = Frame(root)
frame.pack()

labelFrame = LabelFrame(frame, text="Options")
labelFrame.pack()

label = Label(labelFrame, text="Game Mode")
label.grid(column=1, row=0)

var = IntVar()

radio_button_1 = Radiobutton(labelFrame, text="Player vs Computer", variable=var, value=1)
radio_button_1.grid(column=1, row=1)

# radio_button_2 = Radiobutton(labelFrame, text="Player vs Player", variable=var, value=2)
# radio_button_2.grid(column=2, row=1)

button = Button(labelFrame, text="PLAY!!", command=option)
button.grid(column=1, row=2)

animation_label = Label(root)
animation_label.pack()

def animate(index):
    frame = frames[index]
    animation_label.config(image=frame)
    root.after(100, animate, (index + 1) % len(frames))

animate(0)

root.mainloop()