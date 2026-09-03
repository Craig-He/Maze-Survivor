#Main.py

#Importing libraries
import sys
import random
import tkinter as tk
from tkinter import *

#File path of DrawMaze.py
sys.path.insert(1, "C:\\PROJECT\\DrawMaze.py")

#Imports the DrawMaze.py from it being imported from the sys.path function
import DrawMaze

#Class which makes the main menu using Tkinter
class startMenu ():
    def __init__(self):
    #Initiates the class by setting the attribute self.timer to 60 and running the method buildMenu
        self.timer = 60
        self.buildMenu()
        

        
        
        
        
        
    #Method that builds the main menu using Tkinter
    def buildMenu(self):
        #Creating the main menu window using Tkinter, while also setting the window name and it's dimensions
        self.window = tk.Tk()
        self.window.title('Maze Survivor')
        self.window.geometry("1280x720")

        #Setting up the background of main menu
        #Using the PhotoImage function MenuBackground.png is stored in background
        background = PhotoImage(file = "C:\\PROJECT\\GUI\\MenuBackground.png")

        #Using the Label and .place functions, the bg label is created which is the image stored in background displayed in the window of the main menu
        bg = Label(self.window, image = background)
        bg.place(x = 0, y = 0)

        #Setting up the Play Game button
        #Using the PhotoImage function PlayGameButton.png is stored in PlayGameGUI
        PlayGameGUI = PhotoImage(file = "C:\\PROJECT\\GUI\\PlayGameButton.png")

        #Using the Button and .place functions the Play Game button is created which is displayed in the window of the main menu
        #The image of the button is the image stored in PlayGameGUI
        #When the button is pressed it runs the method startGame
        self.PlayGameButton = Button(self.window, image = PlayGameGUI, command = self.startGame)
        self.PlayGameButton.place(x = 50, y = 175)

        #Setting up the Quit Game button
        #Using the PhotoImage function QuitButton.png is stored in QuitGameGUI
        QuitGameGUI = PhotoImage(file = "C:\\PROJECT\\GUI\\QuitButton.png")

        #Using the Button and .place functions the Quit Game button is created which is displayed in the window of the main menu
        #The image of the button is the image stored in QuitGameGUI
        #When the button is pressed it runs the method quitGame
        self.QuitGameButton =  Button(self.window, image = QuitGameGUI, command = self.quitGame)
        self.QuitGameButton.place(x = 730, y = 175)

        #Setting up the Easy Difficulty button
        #Using the PhotoImage function Easy button.png is stored in EasyGUI
        EasyGUI = PhotoImage(file = "C:\\PROJECT\\GUI\\Easy button.png")

        #Using the Button and .place functions the Easy Difficulty button is created which is displayed in the window of the main menu
        #The image of the button is the image stored in EasyGUI
        #When the button is pressed it runs the method setDifficultyEasy
        EasyButton = Button(self.window, image = EasyGUI, command = self.setDifficultyEasy)
        EasyButton.place(x = 400, y = 600)
        
        #Setting up the Medium Difficulty button
        #Using the PhotoImage function Medium button.png is stored in MediumGUI
        MediumGUI = PhotoImage(file = "C:\\PROJECT\\GUI\\Medium button.png")

        #Using the Button and .place functions the Medium Difficulty button is created which is displayed in the window of the main menu
        #The image of the button is the image stored in MediumGUI
        #When the button is pressed it runs the method setDifficultyMedium
        MediumButton = Button(self.window, image = MediumGUI, command = self.setDifficultyMedium)
        MediumButton.place(x = 600, y = 600)

        #Setting up the Hard Difficulty button
        #Using the PhotoImage function Hard button.png is stored in HardGUI
        HardGUI = PhotoImage(file = "C:\\PROJECT\\GUI\\Hard button.png")

        #Using the Button and .place functions the Hard Difficulty button is created which is displayed in the window of the main menu
        #The image of the button is the image stored in HardGUI
        #When the button is pressed it runs the method setDifficultyHard
        HardButton = Button(self.window, image = HardGUI, command = self.setDifficultyHard )
        HardButton.place(x = 800, y = 600)

                
        #Tkinter function that runs the while loop to keep the main menu window responsive
        self.window.mainloop()
        
        
    #Method that destroys the main window menu if the Quit Game button is pressed using the .destroy function
    def quitGame(self):
        self.window.destroy()

    #Method that updates the timer attribute to be 60 seconds
    def setDifficultyEasy(self):
        self.timer = 60
        print("Timer now equals 60")
        

    #Method that updates the timer attribute to be 120 seconds
    def setDifficultyMedium(self):
        self.timer = 120
        print("Timer now equals 120")


    #Method that updates the timer attribute to be 180 seconds
    def setDifficultyHard(self): 
        self.timer = 180
        print("Timer now equals 180")
        
    #Method returns the attribute timer
    def returnTimer(self):
        return self.timer

    #Method that starts the game if the Play Game button is pressed
    def startGame(self):
        #Destroys the main window menu
        self.window.destroy()

        #attribute that stores the value of the timer by running the method return Timer
        self.GetTimer = self.returnTimer()

        #Declares gameManger as the memory location for the GameManger Class
        #The GameManager Class is then initiated with GetTimer as one of it's parameters
        gameManager = GameManager(self.GetTimer)
        
        
#Class which sets up and runs the game
class GameManager():
    def __init__(self,timer):
        #Initiates the class, which starts the game.

        #Creates the attribute timer, which holds the value stored in the timer parameter
        #The timer parameter will hold the value of GetTimer from the startMenu class when the program is executed
        self.timer = timer

        #Declares DrawMaze as the memory location for the DrawMaze Class from DrawMaze.py, Initiating the class
        drawMaze = DrawMaze.DrawMaze()

        #Sets up the parmeters to be used in the various classes by using getter methods from the DrawMaze class

        #Stores the self.theMaze attribute from the DrawMaze class into gameMaze
        gameMaze = drawMaze.returnMaze()

        #Gets the self.theMaze attribute from the DrawMaze class and stores it into gameMaze
        gameWindow = drawMaze.returnGameWindow()

        #Gets the self.gameCanvas attribute from the DrawMaze class and stores it into gameCanvas
        gameCanvas = drawMaze.returnCanvas()

        #Gets the self.runnerLocation attribute from the DrawMaze class and stores it into runnerLocation so it contains the runner sprite
        runnerLocation = drawMaze.returnRunnerLocation()

        #Gets the self.taggerLocation attribute from the DrawMaze class and stores it into runnerLocation so it contains the tagger sprite
        taggerLocation = drawMaze.returnTaggerLocation()


        #Declares runner as the memory location for the Runner class
        #Initiating the class with the parameters gameMaze, GameCanvas and runnerLocation so the Runner's position in the maze can be updated when it moves
        #drawMaze is also a parameter so methods from the DrawMaze class can be used used to find the starting position of the Runner
        runner = Runner(gameMaze, gameCanvas, runnerLocation, drawMaze)

        #Declares runner as the memory location for the Runner class
        #Initiating the class with the parameters gameMaze, gameCanvas and runnerLocation so the Tagger's position can be updated when it moves
        #drawMaze is also a parameter so methods from the DrawMaze class can be used to find the starting position of the Tagger
        tagger = Tagger(gameMaze,gameCanvas,taggerLocation,drawMaze)

        #Declares gameEndChec as the memory location for the GameEndCheck class
        #Initiating the class with the parameters gameCanvas and gameWindow so the class can use Tkinter to create the timer
        #self.timer is also a parameter to determine how long the timer is
        #runner and tagger are parameters so methods from both class can be used to find their positions in the maze to see if the Tagger has caught the Runner
        gameEndChec = GameEndCheck(gameWindow, gameCanvas,self.timer,runner,tagger)


        
        

          

        

    
            
            
            
            
           


        
        
        

        
        




#Class which manages the operations of the runner
class Runner():
    def __init__(self, gameMaze, gameCanvas, runnerLocation, drawMaze):
    #Initiates the class

        #Creates the attribute self.runnerPosInMaze which holds the value stored in the gameMaze parameter
        #The gameMaze parameter will hold the contents of gameMaze from the GameManager class when the program is executed
        self.runnerPosInMaze = gameMaze

        #Creates the attribute self.gameCanvas which holds the value stored in the gameCanvas parameter
        #The gameCanvas parameter will hold the contents of gameCanvas from the GameManager class when the program is executed
        self.gameCanvas = gameCanvas
        
        #Creates the attribute self.runnerLocation which holds the value stored in the runnerLocation parameter
        #The runnerLocation parameter will hold the contents of runnerLocation from the GameManager class when the program is executed
        self.runnerLocation = runnerLocation

        #Creates the attribute self.drawMaze which holds the value stored in the drawMaze parameter
        #The drawMaze parameter holds the contents of drawMaze from the GameManager class when the program is executed
        #This means self.drawMaze contains the DrawMaze Class so it can use it's methods to get the runner's starting position
        self.drawMaze = drawMaze

        #Runs the method movement
        self.movement()

    #Method that gets the position of the runner in the Maze
    def movement(self):

        #Using the method from the DrawMaze class, it gets the runner's position in the Y-axis of the maze (Row of the 2D-array)
        self.runnerPositionY =  self.drawMaze.returnRunnerPositionY()

        #Using the method from the DrawMaze class, it gets the runner's position in the X-axis of the maze (Column of the 2D-array)
        self.runnerPositionX =  self.drawMaze.returnRunnerPositionX()

        #Sets up the keybind for the W-key using the .bind function
        #This means every time the W-key is pressed it will run the method keyPressW
        self.gameCanvas.bind("<w>", self.keyPressW)
        self.gameCanvas.bind("<W>", self.keyPressW)

        #Sets up the keybind for the S-key using the .bind function
        #This means every time the S-key is pressed it will run the method keyPressS
        self.gameCanvas.bind("<s>", self.keyPressS)
        self.gameCanvas.bind("<S>", self.keyPressS)

        #Sets up the keybind for the A-key using the .bind function
        #This means every time the A-key is pressed it will run the method keyPressA
        self.gameCanvas.bind("<a>", self.keyPressA)
        self.gameCanvas.bind("<A>", self.keyPressA)

        #Sets up the keybind for the D-key using the .bind function
        #This means every time the D-key is pressed it will run the method keyPressD
        self.gameCanvas.bind("<d>", self.keyPressD)
        self.gameCanvas.bind("<D>", self.keyPressD)

        #Activates the keybinds using the .focus_set function
        self.gameCanvas.focus_set()

    #Method that disables the Runner's movement keys when the game ends
    def stopRunner(self):
        #Deactivates the keybind for the W-key using the .unbind function so the runner can no longer move up
        self.gameCanvas.unbind("<w>")
        self.gameCanvas.unbind("<W>")

        #Deactivates the keybind for the S-key using the .unbind function so the runner can no longer move down
        self.gameCanvas.unbind("<s>")
        self.gameCanvas.unbind("<S>")

        #Deactivates the keybind for the A-key using the .unbind function so the runner can no longer move left
        self.gameCanvas.unbind("<a>")
        self.gameCanvas.unbind("<A>")

        #Deactivates the keybind for the D-key using the .unbind function so the runner can no longer move right
        self.gameCanvas.unbind("<d>")
        self.gameCanvas.unbind("<D>")
        

        
    #Method that is run when the W-key is pressed
    def keyPressW(self,event):

        #Checks if the runner can move up
        #If there is a path ahead, the runner moves up the maze and the place where it just was is set to a path
        if self.runnerPosInMaze[self.runnerPositionY-1][self.runnerPositionX] == 'P':
            self.runnerPosInMaze[self.runnerPositionY-1][self.runnerPositionX] = 'runner'
            self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX] = 'P'

            #Moves the Runner sprite up using the Tkinter function .move by the coordinate (0, -15) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.runnerLocation, 0, -15)

            #Updates the Runner position in the Y-axis of the maze (Row of the 2D-array)
            self.runnerPositionY = self.runnerPositionY - 1
            
    #Method that is run when the S-key is pressed
    def keyPressS(self,event):

        #Checks if the runner can move down
        #If there is a path ahead, the runner moves down the maze and the place where it just was is set to a path in the 2D-array
        if self.runnerPosInMaze[self.runnerPositionY+1][self.runnerPositionX] == 'P':
            self.runnerPosInMaze[self.runnerPositionY+1][self.runnerPositionX] = 'runner'
            self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX] = 'P'

            #Moves the Runner sprite down using the Tkinter function .move by the coordinate (0, 15) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.runnerLocation, 0, 15)

            #Updates the Runner position in the Y-axis of the maze (Row of the 2D-array)
            self.runnerPositionY = self.runnerPositionY + 1
    

    #Method that is run when the A-key is pressed
    def keyPressA(self,event):

        #Checks if the runner can move left
        #If there is a path ahead, the runner moves left in the maze and the place where it just was is set to a path in the 2D-array
        if self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX-1] == 'P':
            self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX-1] = 'runner'
            self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX] = 'P'

            #Moves the Runner sprite left using the Tkinter function .move by the coordinate (-15, 0) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.runnerLocation, -15,0)

            #Updates the Runner position in the X-axis of the maze (Column of the 2D-array)
            self.runnerPositionX = self.runnerPositionX - 1
            
    #Method that is run when the D-key is pressed
    def keyPressD(self,event):

        #Checks if the runner can move right
        #If there is a path, the runner moves right in the maze and the place where it just was is set to a path in the 2D-array
        if self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX+1] == 'P':
            self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX+1] = 'runner'
            self.runnerPosInMaze[self.runnerPositionY][self.runnerPositionX] = 'P'

            #Moves the Runner sprite right using the Tkinter function .move by the coordinate (15, 0) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.runnerLocation, 15,0)

            #Updates the Runner position in the X-axis of the maze (Column of the 2D-array)
            self.runnerPositionX = self.runnerPositionX + 1
            

    #Method that returns the runner's position in the Y-axis of the maze (Row of the 2D-array)
    def returnRunnerPositionY(self):
        return self.runnerPositionY

    #Method that returns the runner's position in the X-axis of the maze (Column of the 2D-array)
    def returnRunnerPositionX(self):
        return self.runnerPositionX
        

            

            
  
class Tagger():
    def __init__(self,gameMaze, gameCanvas, taggerLocation, drawMaze):
    #Initiates the class

        #Creates the attribute self.taggerPosInMaze which holds the value stored in the gameMaze parameter
        #The gameMaze parameter will hold the contents of gameMaze from the GameManager class when the program is executed
        self.taggerPosInMaze = gameMaze

        #Creates the attribute self.runnerPosInMaze which holds the value stored in the runnerLocation parameter
        #The gameCanvas parameter will hold the contents of gameCanvas from the GameManager class when the program is executed
        self.gameCanvas = gameCanvas

        #Creates the attribute self.taggerLocation which holds the value stored in the taggerLocation parameter
        #The taggerLocation parameter will hold the contents of runnerLocation from the GameManager class when the program is executed
        self.taggerLocation = taggerLocation

        #Creates the attribute self.drawMaze which holds the value stored in the drawMaze parameter
        #The drawMaze parameter holds the contents of drawMaze from the GameManager class when the program is executed
        #This means self.drawMaze contains the DrawMaze Class so it can use it's methods to get the runner's starting position in the Maze        
        self.drawMaze = drawMaze

        #Runs the method movement
        self.movement()

    def movement(self):

        #Using the method from the DrawMaze class, it gets the tagger's position in the Y-axis of the maze (Row of the 2D-array)
        self.taggerPositionY =  self.drawMaze.returnTaggerPositionY()

        #Using the method from the DrawMaze class, it gets the tagger's position in the X-axis of the maze (Column of the 2D-array)
        self.taggerPositionX =  self.drawMaze.returnTaggerPositionX()

        #Sets up the keybind for the I-key using the .bind function
        #This means every time the I-key is pressed it will run the method keyPressI
        self.gameCanvas.bind("<i>", self.keyPressI)
        self.gameCanvas.bind("<I>", self.keyPressI)

        #Sets up the keybind for the K-key using the .bind function
        #This means every time the K-key is pressed it will run the method keyPressK
        self.gameCanvas.bind("<k>", self.keyPressK)
        self.gameCanvas.bind("<K>", self.keyPressK)

        #Sets up the keybind for the J-key using the .bind function
        #This means every time the J-key is pressed it will run the method keyPressJ
        self.gameCanvas.bind("<j>", self.keyPressJ)
        self.gameCanvas.bind("<J>", self.keyPressJ)

        #Sets up the keybind for the L-key using the .bind function
        #This means every time the L-key is pressed it will run the method keyPressL
        self.gameCanvas.bind("<l>", self.keyPressL)
        self.gameCanvas.bind("<L>", self.keyPressL)

        #Activates the keybinds using the .focus_set function        
        self.gameCanvas.focus_set()

    def stopTagger(self):
        #Deactivates the keybind for the I-key using the .unbind function so the tagger can no longer move up
        self.gameCanvas.unbind("<i>")
        self.gameCanvas.unbind("<I>")

        #Deactivates the keybind for the K-key using the .unbind function so the tagger can no longer move down
        self.gameCanvas.unbind("<k>")
        self.gameCanvas.unbind("<K>")

        #Deactivates the keybind for the J-key using the .unbind function so the runner can no longer move left
        self.gameCanvas.unbind("<j>")
        self.gameCanvas.unbind("<J>")

        #Deactivates the keybind for the L-key using the .unbind function so the runner can no longer move right
        self.gameCanvas.unbind("<l>")
        self.gameCanvas.unbind("<L>")

        #Runs the method in the DrawMaze class which destroys the game window when the game is over
        self.drawMaze.destroyGameWindow()
        
        


    

    #Method that is run when the I-key is pressed
    def keyPressI(self,event):

        #Checks if the tagger can move up
        #If there is a path or the runner ahead, the tagger moves up the maze and the place where it just was is set to a path
        if self.taggerPosInMaze[self.taggerPositionY-1][self.taggerPositionX] == 'P'or self.taggerPosInMaze[self.taggerPositionY-1][self.taggerPositionX] == 'runner':
            self.taggerPosInMaze[self.taggerPositionY-1][self.taggerPositionX] = 'tagger'
            self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX] = 'P'

            #Moves the Tagger sprite up using the Tkinter function .move by the coordinate (0, -15) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.taggerLocation, 0, -15)

            #Updates the Runner position in the Y-axis of the maze (Row of the 2D-array)
            self.taggerPositionY = self.taggerPositionY - 1

    #Method that is run when the K-key is pressed
    def keyPressK(self,event):

        #Checks if the tagger can move down
        #If there is a path or the runner ahead, the tagger moves down the maze and the place where it just was is set to a path
        if self.taggerPosInMaze[self.taggerPositionY+1][self.taggerPositionX] == 'P' or self.taggerPosInMaze[self.taggerPositionY+1][self.taggerPositionX] == 'runner':
            self.taggerPosInMaze[self.taggerPositionY+1][self.taggerPositionX] = 'tagger'
            self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX] = 'P'


            #Moves the Tagger sprite up using the Tkinter function .move by the coordinate (0, 15) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.taggerLocation, 0, 15)

            #Updates the Runner position in the Y-axis of the maze (Row of the 2D-array)
            self.taggerPositionY = self.taggerPositionY + 1

    #Method that is run when the J-key is pressed
    def keyPressJ(self,event):

        #Checks if the tagger can move left
        #If there is a path or the runner ahead, the tagger moves left in the maze and the place where it just was is set to a path
        if self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX-1] == 'P'or self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX-1] == 'runner':
            self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX-1] = 'tagger'
            self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX] = 'P'

            #Moves the Tagger sprite up using the Tkinter function .move by the coordinate (-15,0) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.taggerLocation, -15,0)

            #Updates the Tagger position in the X-axis of the maze (Column of the 2D-array)
            self.taggerPositionX = self.taggerPositionX - 1

    #Method that is run when the L-key is pressed
    def keyPressL(self,event):

        #Moves the Tagger sprite up using the Tkinter function .move by the coordinate (0, 15) (15 is the constant used for square size which is used in DrawMaze.py)
        if self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX+1] == 'P'or self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX+1] == 'runner':
            self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX+1] = 'tagger'
            self.taggerPosInMaze[self.taggerPositionY][self.taggerPositionX] = 'P'

            #Moves the Tagger sprite up using the Tkinter function .move by the coordinate (15,0) (15 is the constant used for square size which is used in DrawMaze.py)
            self.gameCanvas.move(self.taggerLocation, 15,0)

            #Updates the Tagger position in the X-axis of the maze (Column of the 2D-array)
            self.taggerPositionX = self.taggerPositionX + 1

    #Method that returns the tagger's position in the Y-axis of the maze (Row of the 2D-array)
    def returnTaggerPositionY(self):
        return self.taggerPositionY

    #Method that returns the tagger's position in the X-axis of the maze (Column of the 2D-array)
    def returnTaggerPositionX(self):
        return self.taggerPositionX
   


class GameEndCheck():
    def __init__(self, gameWindow, gameCanvas, timer, runner, tagger):
       #Initiates the class

        #Creates the attribute self.gameWindow which holds the value stored in the gameWindow parameter
        #The gameWindow parameter will hold the contents of gameWindow from the GameManager class when the program is executed
        self.gameWindow = gameWindow

        #Creates the attribute self.timer which holds the value stored in the timer parameter
        #The timer parameter will hold the contents of timer from the GameManager class when the program is executed
        self.timer = timer
        
        #Creates the attribute self.gameCanvas which holds the value stored in the gameCanvas parameter
        #The gameCanvas parameter will hold the contents of gameCanvas from the GameManager class when the program is executed
        self.gameCanvas = gameCanvas

        #Runs the method createTimer
        self.createTimer()

        #Creates the attribute self.runner which holds the value stored in the runner parameter
        #The runner parameter holds the contents of runner from the GameManager class when the program is executed
        #This means self.runner contains the Runner Class so it can use it's methods to get the runner's current position in the maze             
        self.runner = runner

        #Creates the attribute self.tagger which holds the value stored in the tagger parameter
        #The tagger parameter holds the contents of tagger from the GameManager class when the program is executed
        #This means self.tagger contains the Tagger Class so it can use it's methods to get the taggers's current position in the maze 
        self.tagger = tagger

        #Creates the attribute self.gameEnd which is set to False and will become True if the conditions are met for the game to end
        self.gameEnd = False

        #Runs the method runTimer, that uses self.timer as the parameter for timeleft in the runTimer method
        self.runTimer(self.timer)

    #Method the creates the GUI for the timer using Tkinter
    def createTimer(self):
        #Using the Label and .place functions, it creates the Timer button is made which will display the value of self.timer to show how many seconds are left
        self.timerButton = tk.Label(self.gameWindow, text = str(self.timer), bg = "black", height = 3, width = 10, font = "Arial", fg = "white")
        self.timerButton.place(x = 1100, y = 30)

    #Method that uses recursion to operate the timer
    #The parameter timeleft will hold the value stored in self.timer
    def runTimer(self,timeleft):
        #Checks to see if the timer has hit 0 or if the value gameEnd is True
        if timeleft > 0 and self.gameEnd == False:
            #Takes away 1 from time left
            timeleft = timeleft - 1
            
            #Runs the method winCheck
            self.winCheck()
            
            #Updates the timer to show the new value
            self.timerButton.config(text = str(timeleft))

            
            #Using the Tkinter function.after, there will be a 1 second pause (1000 milliseconds) and then will run the method runTimer with the parameter of timeleft
            self.gameCanvas.after(1000, self.runTimer, timeleft)

        #Else the tagger has caught the player or the timer hits zero
        else:
            #Sets the value of self.gameEnd to True
            self.gameEnd = True

            #Removes sets the timer to show nothing and then the timer is removed from the screen using the .destroy function
            self.timerButton.config(text = "")
            self.timerButton.destroy()

            #Runs the method in the Runner class stopRunner so the Runner can no longer move
            self.runner.stopRunner()

            #Runs the method in the Tagger class stopTagger so the Tagger can no longer move
            self.tagger.stopTagger()

            #Runs the method runnerWins which will display the Runner Wins Menu
            self.runnerWins()
            
    #Method that is run every second to check if the tagger has found the player
    def winCheck(self):
        
        #Using the method returnRunnerPositionY from the Runner Class, which will store the runner's position in the Y-axis of the maze into runnerPositionY
        runnerPositionY = self.runner.returnRunnerPositionY()

        #Using the method returnRunnerPositionX from the Runner Class, which will store the runner's position in the X-axis of the maze into runnerPositionX
        runnerPositionX = self.runner.returnRunnerPositionX()

        #Using the method returnTaggerPositionY from the Tagger Class, which will store the tagger's position in the Y-axis of the maze into taggerPositionY
        taggerPositionY  = self.tagger.returnTaggerPositionY()

        #Using the method returnTaggerPositionX from the Tagger Class, which will store the tagger's position in the X-axis of the maze into taggerPositionX
        taggerPositionX = self.tagger.returnTaggerPositionX()

        #Checks to see if the tagger's position in the maze is equal to the position to the runner.
        if taggerPositionY == runnerPositionY and taggerPositionX == runnerPositionX:
            #If equal then the game is over
            #Sets the value of self.gameEnd to True
            self.gameEnd = True

            #Runs the method in the Runner class stopRunner so the Runner can no longer move
            self.runner.stopRunner()

            #Runs the method in the Tagger class stopTagger so the Tagger can no longer move
            self.tagger.stopTagger()

            #Runs the method taggerWins which will display the Tagger Wins Menu
            self.taggerWins()

    def runnerWins(self):
        #Creating the Runner Wins Menu window using Tkinter, while also setting the window name and it's dimensions
        self.winMenu = tk.Tk()
        self.winMenu.title('Maze Survivor')
        self.winMenu.geometry("1280x800")

        #Setting up the background of Runner wins menu
        #Using the PhotoImage function RunnerWins.png is stored in RunnerWinImage
        RunnerWinImage = PhotoImage(file = "C:\\PROJECT\\GUI\\RunnerWins.png")

        #Using the Label and .place functions, the RunnerWins label is created which is the image stored in RunnerWinImage displayed in the window of the Runner Wins Menu
        RunnerWins = Label(self.winMenu, image = RunnerWinImage)
        RunnerWins.place(x = 0, y = 0)

        #Setting up the Menu button
        #Using the PhotoImage function MENU.png is stored in MenuGUI
        MenuGUI = PhotoImage(file ="C:\\PROJECT\\GUI\\MENU.png")

        #Using the Button and .place functions the Menu button is created which is displayed in the window of the Runner Wins Menu
        #The image of the button is the image stored in MenuGUI
        #When the button is pressed it runs the method backToMenu
        MenuButton = Button(self.winMenu, image = MenuGUI, command = self.backToMenu)
        MenuButton.place(x = 50, y = 300)


        #Setting up the Quit button
        #Using the PhotoImage function QuitButton.png is stored in QuitGUI
        QuitGUI = PhotoImage(file = "C:\\PROJECT\\GUI\\QuitButton.png")

        #Using the Button and .place functions the Menu button is created which is displayed in the window of the Runner Wins Menu
        #The image of the button is the image stored in QuitGUI
        #When the button is pressed it runs the method Quit
        QuitButton = Button(self.winMenu, image = QuitGUI, command = self.Quit)
        QuitButton.place(x = 730 , y = 300)

        
        #Tkinter function that runs the while loop to keep the Runner Wins Menu window responsive
        self.winMenu.mainloop()


    def taggerWins(self):
        #Creating the Tagger Wins Menu window using Tkinter, while also setting the window name and it's dimensions
        self.winMenu = tk.Tk()
        self.winMenu.title('Maze Survivor')
        self.winMenu.geometry("1280x800")

        #Setting up the background of Tagger Wins Menu
        #Using the PhotoImage function TaggerWins.png is stored in TaggerWinImage
        TaggerWinImage = PhotoImage(file = "C:\\PROJECT\\GUI\\TaggerWins.png")

         #Using the Label and .place functions, the TaggerWins label is created which is the image stored in TaggerWinImage displayed in the window of the Tagger Wins Menu
        TaggerWins = Label(self.winMenu, image = TaggerWinImage)
        TaggerWins.place(x = 0, y = 0)

        #Setting up the Menu button
        #Using the PhotoImage function MENU.png is stored in MenuGUI
        MenuGUI = PhotoImage(file ="C:\\PROJECT\\GUI\\MENU.png")

        #Using the Button and .place functions the Menu button is created which is displayed in the window of the Tagger Wins Menu
        #The image of the button is the image stored in MenuGUI
        #When the button is pressed it runs the method backToMenu
        MenuButton = Button(self.winMenu, image = MenuGUI, command = self.backToMenu)
        MenuButton.place(x = 50, y = 300)

        #Using the Button and .place functions the Menu button is created which is displayed in the window of the Tagger Wins Menu
        #The image of the button is the image stored in QuitGUI
        #When the button is pressed it runs the method Quit
        QuitGUI = PhotoImage(file = "C:\\PROJECT\\GUI\\QuitButton.png")
        QuitButton = Button(self.winMenu, image = QuitGUI, command = self.Quit)
        QuitButton.place(x = 730 , y = 300)

        #Tkinter function that runs the while loop to keep the Runner Wins Menu window responsive
        self.winMenu.mainloop()
        
    def backToMenu(self):
        self.winMenu.destroy()
        backToMenu = startMenu()

    #Method that destroys the Runner Wins Menu if the Quit button is pressed using the .destroy function
    def Quit(self):
        self.winMenu.destroy()
        
           







#Declares menu as the memory location for startMenu Class, which initiates the class and creates the main menu
menu = startMenu()


