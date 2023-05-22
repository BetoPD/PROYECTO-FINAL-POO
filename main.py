from tkinter import *
from battleShipSinglePlayer import *
from multiplayerBattleShip import *

pathVideo = "Haddaway - What Is Love (slowed).mp3"
pathGift = Image.open("mike-o-hearn.gif")
window = None

def play():
    pygame.mixer.music.load(pathVideo)
    pygame.mixer.music.play(loops=5)

def option():
    global window
    value = var.get()
    if not value:
        messagebox.showwarning("Hey dude!!!", "Hey Dude!!!\nChoose an option")
        return

    if window:
        window.destroy()

    pygame.mixer.music.stop()

    if var.get() == 1:
        window = SinglePlayerBattleShip()
    else:
        window = MultiPlayerBattleShip()
    

root = Tk()
root.title("Main Menu")
root.geometry("600x600")
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
radio_button_1.grid(column=0, row=1)

radio_button_2 = Radiobutton(labelFrame, text="Player vs Player", variable=var, value=2)
radio_button_2.grid(column=2, row=1)

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