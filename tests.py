from tkinter import *
import battleShip as bShip

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.new_window = None
        self.game = None
        self.cB()
        self.mainloop()
    
    def cB(self):
        button = Button(self, text="Create Game", command=self.createGame)
        button.pack()
    
    def createGame(self):
        if self.game:
            self.game.destroy()
        
        self.game = bShip.BattleShip(self)
            

root = Main()