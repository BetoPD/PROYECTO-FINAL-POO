from tkinter import *

globalDimensions = 40

# Crear el canvas
# Poner Los cuadros del Mar
# Posicionar el canvas de la manera correcta
# Hacer que el canvas tenga número y texto
# Hacer interfaz de usuario

root = Tk()
root.title("BATTLESHIP")

frame = Frame(root)
frame.pack()

combat_zone = LabelFrame(frame, text="COMBAT ZONE")
combat_zone.grid(column=0, row=0)


canvasMyShips = Canvas(combat_zone, width=globalDimensions*10, height=globalDimensions*10)
canvasMyShips.grid(column=1,row=1)

canvasMyShots = Canvas(combat_zone, width=globalDimensions*10, height=globalDimensions*10)
canvasMyShots.grid(column=3, row=1)

inputZone = LabelFrame(frame)
inputZone.grid(column=0, row=1)

placeBoats = LabelFrame(inputZone, text="PLACE BOATS")
placeBoats.grid(column=0, row=0)

shotBoats = LabelFrame(inputZone, text="Shoot Some Boats")
shotBoats.grid(column=1, row=0)

for widget in  frame.winfo_children():
    widget.grid_configure(pady=20)

# SELECT THE BOAT SIZE


for i in range(6):
    Label(placeBoats, text="Boat {}".format(i + 1)).grid(column=0, row=i)

for i in range(1):
    Label(shotBoats, text="Shoot {}".format(i + 1)).grid(column=0, row=i)

# SELECT THE COORDINATES WHERE TO PLACE IT

coordinate1 = Entry(placeBoats)
coordinate1.grid(column=1, row=0)

coordinate2 = Entry(placeBoats)
coordinate2.grid(column=1, row=1)

coordinate3 = Entry(placeBoats)
coordinate3.grid(column=1, row=2)

coordinate4 = Entry(placeBoats)
coordinate4.grid(column=1, row=3)

coordinate5 = Entry(placeBoats)
coordinate5.grid(column=1, row=4)

coordinate6 = Entry(placeBoats)
coordinate6.grid(column=1, row=5)

# SELECT THE SHOOT ZONE

shot = Entry(shotBoats)
shot.grid(column=1, row=0)
button = Button(shotBoats, text="SHOOOT!!")
button.grid(column=0, row=1, columnspan=2)

# PLACE THE NUMBER AND THE LETTER IN THE COMBAT ZONE

dict = {}
letterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

for i in range(10):
    dict[i] = letterList[i]

canvasNumbers = Canvas(combat_zone, width=globalDimensions* 10, height=globalDimensions)
canvasNumbers.grid(column=1, row=0)

canvasLetter = Canvas(combat_zone, width=globalDimensions, height=globalDimensions * 10)
canvasLetter.grid(column=0, row=1)


for i in range(10):
    canvasNumbers.create_rectangle(i * globalDimensions, 0, (i * globalDimensions) + globalDimensions, globalDimensions, fill='white', outline='red')
    canvasNumbers.create_text(globalDimensions / 2 + (i * globalDimensions), globalDimensions / 2, text='{}'.format(i + 1), font=('Arial', int(globalDimensions * 0.7)), fill='purple')

for i in range(10):
    canvasLetter.create_rectangle(0, i * globalDimensions, globalDimensions, (i * globalDimensions) + globalDimensions, fill='white', outline='red')
    canvasLetter.create_text(globalDimensions / 2, globalDimensions / 2 + (i * globalDimensions), text='{}'.format(dict[i]), font=('Arial', int(globalDimensions * 0.7)), fill='purple')

# FOR THE SHOTS

canvasNumbers2 = Canvas(combat_zone, width=globalDimensions*10, height=globalDimensions)
canvasNumbers2.grid(column=3, row=0)

canvasLetter2 = Canvas(combat_zone, width=globalDimensions, height=globalDimensions * 10)
canvasLetter2.grid(column=2, row=1)


for i in range(10):
    canvasNumbers2.create_rectangle(i * globalDimensions, 0, (i * globalDimensions) + globalDimensions, globalDimensions, fill='white', outline='red')
    canvasNumbers2.create_text(globalDimensions / 2 + (i * globalDimensions), globalDimensions / 2, text='{}'.format(i + 1), font=('Arial', int(globalDimensions * 0.7)), fill='purple')

for i in range(10):
    canvasLetter2.create_rectangle(0, i * globalDimensions, globalDimensions, (i * globalDimensions) + globalDimensions, fill='white', outline='red')
    canvasLetter2.create_text(globalDimensions / 2, globalDimensions / 2 + (i * globalDimensions), text='{}'.format(dict[i]), font=('Arial', int(globalDimensions * 0.7)), fill='purple')

for widget in  inputZone.winfo_children():
    widget.grid_configure(padx=200)


# STARTS

x_axis = 10
y_axis = 10
dx = globalDimensions
dy = globalDimensions



class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = " "
        self.ship = False
    
    def drawMyself(self, color="blue"):
        x = self.x * dx
        y = self.y * dy

        canvasMyShips.create_rectangle(x, y, x + dx, y + dy, fill=color, outline="white")

class CellShot(Cell):
    def drawMyself(self, color="blue"):
        x = self.x * dx
        y = self.y * dy
        canvasMyShots.create_rectangle(x, y, x + dx, y + dy, fill=color, outline="white")

    

# The most common dimensions of a battleship Grid


myShips = [Cell(x, y) for y in range(y_axis) for x in range(x_axis)]
myShots = [CellShot(x, y) for y in range(y_axis) for x in range(x_axis)]

for ship in myShips:
    ship.drawMyself()

for shot in myShots:
    shot.drawMyself()




root.mainloop()
