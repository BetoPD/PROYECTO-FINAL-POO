from battleShip import *

class MultiPlayerBattleShip(BattleShip):

    def __init__(self, globalDimensions=40):
        super().__init__(globalDimensions)
        self.__letterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    def StartingGame(self):
        print("uso al hijo")
        # Creates a dictionary assingning each letter to a numeric value

        translate = {}

        for i in range(0, 10):
            translate[self.__letterList[i]] = i

        # If there already exist coordinates, it will restart them

        if self.coordinateValues:
            self.coordinateValues = []
        
        # Checks every input, to validate the format

        for item in self.coordinateList:
            current_value = item.get()
            
            if (len(current_value) > 2 or not current_value) and current_value[1:] != "10":
                self.warningAndRestart("Incorrect length")
                return
            
            if type(current_value[0]) != str:
                self.warningAndRestart("Input not letter")
                return
            
            numericValue = current_value[1:]
            
            numbersStrings = [str(i) for i in range(1, 11)]

            if numericValue not in numbersStrings:
                self.warningAndRestart("Wrong numbers")
                return
            
            x = int(numericValue)
            y = current_value[0].upper()

            if y not in self.__letterList:
                self.warningAndRestart("Wrong inputs")
                return
            
            coordinates  = (x - 1, translate[y])

            if coordinates in self.coordinateValues:
                self.warningAndRestart("Repeated values detected")
                return
            
            self.coordinateValues.append(coordinates)
        

        # Checking if a value for Horizontal or Vertical is missing

        for item in self.orientationValues:
            current_o_value = item.get()

            if not current_o_value:
                self.warningAndRestart("Missing Values")
                return
        
        # Validating the coordinates, in orther to see if the ship does fit in the grid, or ships are not overlapping between them

        shipsToDraw = []

        for i, coordinate in enumerate(self.coordinateValues):
            currentShip = []
            x = coordinate[0]
            y = coordinate[1]   
            startPoint =  self.myShips[0].index(x, y)
            self.myShips[startPoint].ship = True
            currentShip.append(startPoint)
            for j in range(1, 6 - i):
                if self.orientationValues[i].get() == "H":
                    index = self.myShips[0].index(x + j, y)
                    if not index:
                        self.warningAndRestart("Ship {} does not fit".format(i + 1))
                        return
                    else:
                        if self.myShips[index].ship:
                            self.warningAndRestart("Ship {} overlapping".format(i))
                            return
                        currentShip.append(index)
                        self.myShips[index].ship = True
                else:
                    index = self.myShips[0].index(x, y + j)
                    if not index:
                        self.warningAndRestart("Ship {} does not fit".format(i + 1))
                        return
                    else:
                        if self.myShips[index].ship:
                            self.warningAndRestart("Ship {} overlapping".format(i))
                            return
                        currentShip.append(index)
                        self.myShips[index].ship = True        
            shipsToDraw.append(currentShip)


        #DRAWING THE SHIPS
        
        for ship in shipsToDraw:
            for index in ship:
                self.myShips[index].drawMyself(self.dx, self.dy, self.canvasMyShips, "Purple")

        for item in self.orientationValues:
            print(item.get())

        print(self.coordinateValues)

        # DISABLING EVERYTHING

        self.submitCoordinates.configure(state="disabled")
        
        for item in self.coordinateList:
            item.config(state="disabled") 

        for button in self.radioButtons:
            button.config(state="disabled")
        