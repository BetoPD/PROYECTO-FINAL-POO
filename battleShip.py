from tkinter import *
from tkinter import messagebox
import random 
import pygame
from tkinter import messagebox
from PIL import Image, ImageTk

class BattleShip(Toplevel):

    def __init__(self, globalDimensions = 40):
        self.globalDimensions = globalDimensions
        self.x_axis = 10
        self.y_axis = 10
        self.dx = globalDimensions
        self.dy = globalDimensions
        self.imagePath = "sigma male playlist (motivational workout music) [TubeRipper.com].mp3"

        super().__init__()
        self.title("Battle Ship")
        self.frame = Frame(self)
        self.frame.pack()
        self.myScore = 0
        self.oponentScore = 0

        self.combat_zone = LabelFrame(self.frame, text="COMBAT ZONE")
        self.combat_zone.grid(column=0, row=0)

        self.canvasMyShips = Canvas(self.combat_zone, width=self.globalDimensions*10, height=self.globalDimensions*10)
        self.canvasMyShips.grid(column=1,row=1)

        self.canvasMyShots = Canvas(self.combat_zone, width=self.globalDimensions*10, height=self.globalDimensions*10)
        self.canvasMyShots.grid(column=3, row=1)

        self.inputZone = LabelFrame(self.frame)
        self.inputZone.grid(column=0, row=1)

        self.placeBoats = LabelFrame(self.inputZone, text="PLACE BOATS")
        self.placeBoats.grid(column=0, row=0)

        self.shotBoats = LabelFrame(self.inputZone, text="Shoot Some Boats")
        self.shotBoats.grid(column=1, row=0)

        self.__dict = {}
        self.__letterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.coordinate1 = None
        self.coordinate2 = None
        self.coordinate3 = None
        self.coordinate4 = None
        self.coordinate5 = None
        self.coordinate6 = None
        self.coordinateList = []
        self.coordinateValues = []
        self.orientationValues = []
        self.radioButtons = []
        self.submitCoordinates = None
        self.shot =  None
        self.button = None
        self.canvasNumbers = None
        self.canvasLetter = None
        self.canvasNumbers2 = None
        self.canvasLetter2 = None
        self.myShips = None
        self.myShots = None
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.initializeAll()

    def boatSize(self):

        # A text that tells the size of the boat 6 - 1

        for i in range(6):
            Label(self.placeBoats, text="Boat {}".format(i + 1)).grid(column=0, row=i)

        for i in range(1):
            Label(self.shotBoats, text="Shoot {}".format(i + 1)).grid(column=0, row=i)
    
    def coordinates(self):

        # Entries to decide where to place the ships in the canvas

        self.boatSize()

        self.coordinate1 = Entry(self.placeBoats)
        self.coordinate1.grid(column=1, row=0)
        self.coordinateList.append(self.coordinate1)

        self.coordinate2 = Entry(self.placeBoats)
        self.coordinate2.grid(column=1, row=1)
        self.coordinateList.append(self.coordinate2)

        self.coordinate3 = Entry(self.placeBoats)
        self.coordinate3.grid(column=1, row=2)
        self.coordinateList.append(self.coordinate3)

        self.coordinate4 = Entry(self.placeBoats)
        self.coordinate4.grid(column=1, row=3)
        self.coordinateList.append(self.coordinate4)

        self.coordinate5 = Entry(self.placeBoats)
        self.coordinate5.grid(column=1, row=4)
        self.coordinateList.append(self.coordinate5)

        self.coordinate6 = Entry(self.placeBoats)
        self.coordinate6.grid(column=1, row=5)
        self.coordinateList.append(self.coordinate6)

        self.submitCoordinates = Button(self.placeBoats, text="SUBMIT COORDINATES", command=self.StartingGame)
        self.submitCoordinates.grid(column=1, row=6)
    
    def orientationZone(self):

        # Radio Buttons to choose the orientation of the ships, either Vertical or Horizontal

        for i in range(6):
            var = StringVar()
            self.orientationValues.append(var)
            radio_button_1 = Radiobutton(self.placeBoats, text="Horizontal", variable=var, value="H")
            radio_button_2 = Radiobutton(self.placeBoats, text="Vertical", variable=var, value="V")
            self.radioButtons.append(radio_button_1)
            self.radioButtons.append(radio_button_2)
            radio_button_1.grid(column=2, row=i)
            radio_button_2.grid(column=3, row=i)

    def shotZone(self):

        # Creates an entry and a button to shoot enemy ships:

        self.shot = Entry(self.shotBoats)
        self.shot.grid(column=1, row=0)
        self.button = Button(self.shotBoats, text="SHOOOT!!")
        self.button.grid(column=0, row=1, columnspan=2)

    def initializeDict(self):

        # Creates a dict, where you assing a number as the key, and a letter as the value

        for i in range(10):
            self.__dict[i] = self.__letterList[i]
    
    def placeNumberAndLetter(self):

        # Creates the letters and number squares around the Battle Canvas
        
        self.initializeDict()
        
        self.canvasNumbers = Canvas(self.combat_zone, width=self.globalDimensions* 10, height=self.globalDimensions)
        self.canvasNumbers.grid(column=1, row=0)
        self.canvasLetter = Canvas(self.combat_zone, width=self.globalDimensions, height=self.globalDimensions * 10)
        self.canvasLetter.grid(column=0, row=1)   

        for i in range(10):
            self.canvasNumbers.create_rectangle(i * self.globalDimensions, 0, (i * self.globalDimensions) + self.globalDimensions, self.globalDimensions, fill='white', outline='red')
            self.canvasNumbers.create_text(self.globalDimensions / 2 + (i * self.globalDimensions), self.globalDimensions / 2, text='{}'.format(i + 1), font=('Arial', int(self.globalDimensions * 0.7)), fill='purple')

        for i in range(10):
            self.canvasLetter.create_rectangle(0, i * self.globalDimensions, self.globalDimensions, (i * self.globalDimensions) + self.globalDimensions, fill='white', outline='red')
            self.canvasLetter.create_text(self.globalDimensions / 2, self.globalDimensions / 2 + (i * self.globalDimensions), text='{}'.format(self.__dict[i]), font=('Arial', int(self.globalDimensions * 0.7)), fill='purple')
    
    def placeShots(self):
        
        # Function to see where you have shooted, it is a canvas, similar to the ship canvas

        self.canvasNumbers2 = Canvas(self.combat_zone, width=self.globalDimensions*10, height=self.globalDimensions)
        self.canvasNumbers2.grid(column=3, row=0)

        self.canvasLetter2 = Canvas(self.combat_zone, width=self.globalDimensions, height=self.globalDimensions * 10)
        self.canvasLetter2.grid(column=2, row=1)

        for i in range(10):
            self.canvasNumbers2.create_rectangle(i * self.globalDimensions, 0, (i * self.globalDimensions) + self.globalDimensions, self.globalDimensions, fill='white', outline='red')
            self.canvasNumbers2.create_text(self.globalDimensions / 2 + (i * self.globalDimensions), self.globalDimensions / 2, text='{}'.format(i + 1), font=('Arial', int(self.globalDimensions * 0.7)), fill='purple')

        for i in range(10):
            self.canvasLetter2.create_rectangle(0, i * self.globalDimensions, self.globalDimensions, (i * self.globalDimensions) + self.globalDimensions, fill='white', outline='red')
            self.canvasLetter2.create_text(self.globalDimensions / 2, self.globalDimensions / 2 + (i * self.globalDimensions), text='{}'.format(self.__dict[i]), font=('Arial', int(self.globalDimensions * 0.7)), fill='purple')

        for widget in self.inputZone.winfo_children():
            widget.grid_configure(padx=200)
    
    def initializeShips(self):
        self.myShips = [Cell(x, y) for y in range(self.y_axis) for x in range(self.x_axis)]
        self.myShots = [CellShot(x, y) for y in range(self.y_axis) for x in range(self.x_axis)]

        for ship in self.myShips:
            ship.drawMyself(self.dx, self.dy, self.canvasMyShips)

        for shot in self.myShots:
            shot.drawMyself(self.dx, self.dy, self.canvasMyShots)
    
    def StartingGame(self):
        pass
        # # Creates a dictionary assingning each letter to a numeric value

        # translate = {}

        # for i in range(0, 10):
        #     translate[self.__letterList[i]] = i

        # # If there already exist coordinates, it will restart them

        # if self.coordinateValues:
        #     self.coordinateValues = []
        
        # # Checks every input, to validate the format

        # for item in self.coordinateList:
        #     current_value = item.get()
            
        #     if (len(current_value) > 2 or not current_value) and current_value[1:] != "10":
        #         self.warningAndRestart("Incorrect length")
        #         return
            
        #     if type(current_value[0]) != str:
        #         self.warningAndRestart("Input not letter")
        #         return
            
        #     numericValue = current_value[1:]
            
        #     numbersStrings = [str(i) for i in range(1, 11)]

        #     if numericValue not in numbersStrings:
        #         self.warningAndRestart("Wrong numbers")
        #         return
            
        #     x = int(numericValue)
        #     y = current_value[0].upper()

        #     if y not in self.__letterList:
        #         self.warningAndRestart("Wrong inputs")
        #         return
            
        #     coordinates  = (x - 1, translate[y])

        #     if coordinates in self.coordinateValues:
        #         self.warningAndRestart("Repeated values detected")
        #         return
            
        #     self.coordinateValues.append(coordinates)
        

        # # Checking if a value for Horizontal or Vertical is missing

        # for item in self.orientationValues:
        #     current_o_value = item.get()

        #     if not current_o_value:
        #         self.warningAndRestart("Missing Values")
        #         return
        
        # # Validating the coordinates, in orther to see if the ship does fit in the grid, or ships are not overlapping between them

        # shipsToDraw = []

        # for i, coordinate in enumerate(self.coordinateValues):
        #     currentShip = []
        #     x = coordinate[0]
        #     y = coordinate[1]   
        #     startPoint =  self.myShips[0].index(x, y)
        #     self.myShips[startPoint].ship = True
        #     currentShip.append(startPoint)
        #     for j in range(1, 6 - i):
        #         if self.orientationValues[i].get() == "H":
        #             index = self.myShips[0].index(x + j, y)
        #             if not index:
        #                 self.warningAndRestart("Ship {} does not fit".format(i + 1))
        #                 return
        #             else:
        #                 if self.myShips[index].ship:
        #                     self.warningAndRestart("Ship {} overlapping".format(i))
        #                     return
        #                 currentShip.append(index)
        #                 self.myShips[index].ship = True
        #         else:
        #             index = self.myShips[0].index(x, y + j)
        #             if not index:
        #                 self.warningAndRestart("Ship {} does not fit".format(i + 1))
        #                 return
        #             else:
        #                 if self.myShips[index].ship:
        #                     self.warningAndRestart("Ship {} overlapping".format(i))
        #                     return
        #                 currentShip.append(index)
        #                 self.myShips[index].ship = True        
        #     shipsToDraw.append(currentShip)


        # #DRAWING THE SHIPS
        
        # for ship in shipsToDraw:
        #     for index in ship:
        #         self.myShips[index].drawMyself(self.dx, self.dy, self.canvasMyShips, "Purple")

        # for item in self.orientationValues:
        #     print(item.get())

        # print(self.coordinateValues)

        # # DISABLING EVERYTHING

        # self.submitCoordinates.configure(state="disabled")
        
        # for item in self.coordinateList:
        #     item.config(state="disabled") 

        # for button in self.radioButtons:
        #     button.config(state="disabled")
        
    def restartShips(self):
        for ship in self.myShips:
            ship.ship = False
    
    def warningAndRestart(self, message = "Warning"):

        # Warning function with a message

        messagebox.showwarning("Warning", message)
        self.coordinateValues = []
        self.restartShips()

    def onClosing(self):
        pygame.mixer.music.stop()
        self.destroy()
        
    def backGroundSound(self):
        pygame.mixer.music.load(self.imagePath)
        pygame.mixer.music.play(loops=5)

    def initializeAll(self):

        # Initializing all functions in order
        self.backGroundSound()
        self.coordinates()
        self.orientationZone()
        self.shotZone()
        self.placeNumberAndLetter()
        self.placeShots()
        self.initializeShips()
        
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = " "
        self.ship = False
    
    def drawMyself(self, dx, dy, canvasMyShips, color="blue"):
        x = self.x * dx
        y = self.y * dy
        canvasMyShips.create_rectangle(x, y, x + dx, y + dy, fill=color, outline="white")
    
    def index(self, x, y):
        if ( x < 0 or y < 0 or x > (10 - 1) or y > (10 - 1)):
            return -1

        return x + y  * 10
    
class CellShot(Cell):
    def drawMyself(self,dx, dy, canvasMyShots, color="blue"):
        x = self.x * dx
        y = self.y * dy
        canvasMyShots.create_rectangle(x, y, x + dx, y + dy, fill=color, outline="white")
