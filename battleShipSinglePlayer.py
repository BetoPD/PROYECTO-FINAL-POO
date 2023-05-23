from battleShip import *

class SinglePlayerBattleShip(BattleShip):

    def __init__(self, globalDimensions=40):
        print("You created a single Player Battle Ship Game")
        super().__init__(globalDimensions)
        self.botShips = [Cell(x, y) for y in range(self.y_axis) for x in range(self.x_axis)]
        self.shipsPositioned = False
        self.button.config(command=self.shooting)
        self.__letterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    
    def StartingGame(self):

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
            # startPoint =  self.myShips[0].index(x, y)
            # self.myShips[startPoint].ship = True
            # currentShip.append(startPoint)
            for j in range(0, 6 - i):
                if self.orientationValues[i].get() == "H":
                    index = self.myShips[0].index(x + j, y)
                    print("Trying to insert ship at index {}".format(index))
                    if index < 0:
                        self.warningAndRestart("Ship {} does not fit".format(i + 1))
                        return
                    else:
                        if self.myShips[index].ship:
                            print("False")
                            self.restartShips()
                            self.warningAndRestart("Ship {} is overlapping".format(i + 1))
                            return
                        print("True")
                        currentShip.append(index)
                        self.myShips[index].ship = True
                else:
                    index = self.myShips[0].index(x, y + j)
                    print("Trying to insert ship at index {}".format(index))
                    if index < 0:
                        self.warningAndRestart("Ship {} does not fit".format(i + 1))
                        return
                    else:
                        if self.myShips[index].ship:
                            print("False")
                            self.restartShips()
                            self.warningAndRestart("Ship {} is overlapping".format(i + 1))
                            return
                        print("True")
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
        
        self.StartingBotShips()

        self.shipsPositioned = True

    def shooting(self):

        if not self.shipsPositioned:
            messagebox.showwarning("Warning", "Ships not positioned yet")
            return

        translate = {}

        for i in range(0, 10):
            translate[self.__letterList[i]] = i

        current_value = self.shot.get()
        
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

        xbot = random.randint(0, 9)
        ybot = random.randint(0, 9)

        index = self.myShips[0].index(coordinates[0], coordinates[1])

        if self.botShips[index].ship:
            self.botShips[index].symbol = "X"
            self.myShots[index].drawMyself(self.dx, self.dy, self.canvasMyShots, "red")
            messagebox.showinfo("HIT!!", "PLAYER 1 hitted at position ({},{})".format(x, y))
            self.myScore += 1
            if self.myScore == 21:
                messagebox.showinfo("WOOOOOW", "YOU WON!!!")
                self.shot.config(state="disabled")
                self.button.config(state="disabled")
                
        else:
            self.myShots[index].drawMyself(self.dx, self.dy, self.canvasMyShots, "purple")
        
        indexBot = self.myShips[0].index(xbot, ybot)

        print("Bot coordinates to shot: ({}, {})".format(xbot, ybot))
        print("Bot shoot at index:", indexBot)

        if self.myShips[indexBot].ship:
            self.myShips[indexBot].symbol = "X"
            messagebox.showinfo("BOT HITTED", "Bot hit at position ({},{})".format(xbot, ybot))
            self.oponentScore += 1
            self.myShips[indexBot].drawMyself(self.dx, self.dy, self.canvasMyShips, "red")
            if self.oponentScore == 21:
                messagebox.showinfo("WOOOOOW", "BOT WON!!!")
                self.shot.config(state="disabled")
                self.button.config(state="disabled")

        else:
            messagebox.showinfo("Bot Shooted", "Bot missed at position ({},{})".format(xbot, ybot))
            self.myShips[indexBot].drawMyself(self.dx, self.dy, self.canvasMyShips, "green")

    def generatingRandomThings(self):
        randomCoordinates = []
        randomOrientations = []
        verticalOrHoirzontal = {0: "H", 1: "V"}

        while len(randomCoordinates) < 6:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            orientation = random.randint(0, 1)
            coordinates = (x, y)
            if not coordinates in randomCoordinates:
                randomCoordinates.append(coordinates)
                randomOrientations.append(verticalOrHoirzontal[orientation])
        
        return (randomCoordinates, randomOrientations)

    def StartingBotShips(self):
        
        randomCoordinates, randomOrientations =  self.generatingRandomThings()

        botCoordinates = []

        for i, coordinate in enumerate(randomCoordinates):
            x = coordinate[0]
            y = coordinate[1]   
            # startPoint =  self.botShips[0].index(x, y)
            # self.botShips[startPoint].ship = True
            for j in range(0, 6 - i):
                if randomOrientations[i] == "H":
                    index = self.botShips[0].index(x + j, y)
                    if index < 0:
                        self.restartBotShips()
                        self.StartingBotShips()
                        return
                    else:
                        if self.botShips[index].ship:
                            self.restartBotShips()
                            self.StartingBotShips()
                            return
                        self.botShips[index].ship = True
                        botCoordinates.append(index)
                else:
                    index = self.botShips[0].index(x, y + j)
                    if index < 0:
                        self.restartBotShips()
                        self.StartingBotShips()
                        return
                    else:
                        if self.botShips[index].ship:
                            self.restartBotShips()
                            self.StartingBotShips()
                            return
                        self.botShips[index].ship = True 
                        botCoordinates.append(index)
        
        print("Bot ships indexes: {}".format(botCoordinates))
        print("Bot ships orientations: {}".format(randomOrientations))
        
    def restartBotShips(self):
        for ship in self.botShips:
            ship.ship = False



