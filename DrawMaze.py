#DrawMaze.py

#Importing libraries
import sys
import tkinter as tk
import random
from tkinter import *

#File path of MazeGeneration.py
sys.path.insert(1, "C:\\PROJECT\\MazeGeneration.py")


#imports the MazeGeneration.py from it being imported from the sys.path function
import MazeGeneration

#Class which will be used to draw the Maze using Tkinter
class DrawMaze():
    def __init__(self):
    #Initiates the class by running the methods SetMazeToTextFile and createMaze
        self.SetMazeToTextFile()
        self.createMaze()
        
    
#The method which processes the Generated Maze into a text file so it can be drawn out with Tkinter
    def SetMazeToTextFile(self):
        #Declares mazeGen as the memory location for the MazeGeneration class, 50 is entered as the height and width parameters to set the maze size to 50x50
        mazeGen = MazeGeneration.MazeGeneration(50,50)

        #grid stores the array of the maze which has been generated
        grid = mazeGen.Prims()

        #Creates a text file called GeneratedMaze.txt which contains the array of the maze generated from MazeGeneration.py
        with open('GeneratedMaze.txt' , 'w') as F: 
            for y in range (len(grid)):
                for x in range (len(grid[0])):
                    F.write(str(grid[y][x]) + ' ')
                F.write("\n")
        F.close()

    #The Method which draws the Maze using Tkinter, while also making the game window
    def createMaze(self):
        #Empty Array which will store the contents of GeneratedMaze.txt when it as been read
        self.theMaze = []
        #Creating the game window using Tkinter, while also setting the window name and it's dimensions
        self.gameWindow = tk.Tk()
        self.gameWindow.title('Maze Survivor')
        self.gameWindow.geometry("1280x800")

        #A constant which is used as a scale when setting up the the height and width of each cell in the maze
        SquareSize = 15

        #Opens the text file GeneratedMaze.txt 
        with open('GeneratedMaze.txt' , 'r') as F:
            #for each line in GeneratedMaze.txt it is appended into self.theMaze
            for lines in F.readlines():
                self.theMaze.append(lines.split())
        F.close()

        #Variables storing how many rows and collumns are in the 2D-array of self.theMaze
        row = len(self.theMaze)
        column = len(self.theMaze[0])

        #The height and width of the maze is determined by multiplying row and collumn by squareSize
        Width = row * SquareSize 
        Height = column * SquareSize

        #the self.GameCanvas is created using the Canvas Tkinter Class, this creates an area in the gamewindow for the maze to be drawn
        self.gameCanvas = Canvas(self.gameWindow, width = Width , height = Height)
        self.gameCanvas.pack()

        #Nested FOR loop to draw the maze
        for y in range (len(self.theMaze)):
            for x in range (len(self.theMaze[0])):

                #Goes through every cell in the Maze
                cellType = self.theMaze[y][x]

                #These variables are used as parameters for the create_rectangle Tkinter function so that each cell is drawn as a square
                #The dimensions of each square are made constant by having the y and x coordinate of the cell being multiplyed by squareSize
                #The value of squareSize is then added on to the respective variables which is stored in a different variables.... (NEED HELP TO EXPLAIN THIS BIT)
                yCoordinate1 = y * SquareSize
                yCoordinate2 = yCoordinate1 + SquareSize
                xCoordinate1 = x * SquareSize
                xCoordinate2 =  xCoordinate1 + SquareSize

                #If the current cell in the Maze is a path, then the create_rectangle function will create a green square in the self.GameCanvas to represent a path
                if cellType == 'P':
                   self.gameCanvas.create_rectangle(xCoordinate1, yCoordinate1, xCoordinate2, yCoordinate2,fill = "green", outline = "green")

                #If the current cell in the Maze is a wall or barrier, then the create_rectangle function will create a black square self.GameCanvas to represent a both
                elif cellType == 'b' or cellType == 'w':
                    self.gameCanvas.create_rectangle(xCoordinate1, yCoordinate1, xCoordinate2, yCoordinate2, fill = "black", outline = "black")

        #WHILE loop to to find a location for the Runner in the maze
        StartSpotFound = False
        while StartSpotFound == False:
            #Randomly picks a row and collumn in the maze
            self.runnerPositionY = random.randint(0,(row-1))
            self.runnerPositionX = random.randint(0,(column-1))

            #If the coordinate is equal to a path then set that cell to Runner
            if self.theMaze[self.runnerPositionY][self.runnerPositionX] == 'P':
                self.theMaze[self.runnerPositionY][self.runnerPositionX] = 'Runner'
                
                StartSpotFound = True

        #More variables which are the parameters for the create_rectangle Tkinter function so that the Runner sprite can be drawn
        startSpotYCoordinate1 = self.runnerPositionY * SquareSize
        startSpotYCoordinate2 =  startSpotYCoordinate1 + SquareSize
        startSpotXCoordinate1 = self.runnerPositionX * SquareSize
        startSpotXCoordinate2 = startSpotXCoordinate1 + SquareSize

        #The attribute self.runnerLocation which stores the Runner sprite, which is created as blue square on the self.GameCanvas to represent the runner
        self.runnerLocation = self.gameCanvas.create_rectangle(startSpotXCoordinate1,  startSpotYCoordinate1,  startSpotXCoordinate2,  startSpotYCoordinate2, fill = "blue", outline = "blue")

        #WHILE loop to to find a location for the Tagger in the Maze
        TaggerSpotFound = False
        while TaggerSpotFound == False:
            #Randomly picks a row and collumn in the maze
            self.taggerPositionY = random.randint(0,(row-1))
            self.taggerPositionX = random.randint(0,(column-1))

            #If the coordinate is equal to a path then set that cell to tagger
            if self.theMaze[self.taggerPositionY][self.taggerPositionX] == 'P':
                self.theMaze[self.taggerPositionY][self.taggerPositionX] = 'tagger'
                TaggerSpotFound = True

        #More variables which are the parameters for the create_rectangle Tkinter function so that the Runner sprite can be drawn
        taggerSpotYCoordinate1 = self.taggerPositionY * SquareSize
        taggerSpotYCoordinate2 = taggerSpotYCoordinate1 + SquareSize
        taggerSpotXCoordinate1 = self.taggerPositionX * SquareSize
        taggerSpotXCoordinate2 = taggerSpotXCoordinate1 + SquareSize

        #The attribute self.taggerLocation which stores the tagger sprite, which is created as red square on the self.GameCanvas to represent the tagger
        self.taggerLocation = self.gameCanvas.create_rectangle(taggerSpotXCoordinate1,  taggerSpotYCoordinate1, taggerSpotXCoordinate2,  taggerSpotYCoordinate2, fill = "Red", outline = "Red")

    #Method that returns the 2D-array of the Maze in its current state
    def returnMaze(self):
        return self.theMaze

    #Method that returns the GameCanvas in its current state
    def returnCanvas(self):
        return self.gameCanvas

    #Method that returns the attribute that holds the runner sprite
    def returnRunnerLocation(self):
        return self.runnerLocation

    #Method that returns the runner's position in the Y-axis of the maze (Row of the 2D-array)
    def returnRunnerPositionY(self):
        return self.runnerPositionY

    #Method that returns the runner's position in the X-axis of the maze (Column of the 2D-array)
    def returnRunnerPositionX(self):
        return self.runnerPositionX

    #Method that returns the attribute that holds the tagger sprite
    def returnTaggerLocation(self):
        return self.taggerLocation

    #Method that returns the tagger's position in the Y-axis of the maze (Row of the 2D-array)
    def returnTaggerPositionY(self):
        return self.taggerPositionY

    #Method that returns the tagger's position in the X-axis of the maze (Column of the 2D-array)
    def returnTaggerPositionX(self):
        return self.taggerPositionX

    #Method that destroys the game window for when the game is over
    def destroyGameWindow(self):
        self.gameWindow.destroy()

#Method that returns the game window in it's current state
    def returnGameWindow(self):
        return self.gameWindow
    


                
        
        








            
        
        
        
    







