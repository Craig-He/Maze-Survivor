#MazeGeneration.py

import random 


#Inniates the class MazeGeneration, this class will be used to generate the maze
class MazeGeneration:
    #Defining the attributes of the Maze generation object
    def __init__(self,height, width, grid =None): 
        self.height = height 
        self.width = width

        #grid is the where the maze data is stored in the 2d array, this is modifyed
        self.grid = grid 

        

#The method which creates a 2D-array which will be the grid that will be put into the Maze generation algorithm
    def createMaze(self):
        #Sets all of the cells in the grid to barriers
        self.grid = [["b" for x in range(self.width)] for y in range(self.height)]
        for y in range(2,self.height-2):
            for x in range(2,self.width-2):
                #sets everything but the last two layers of cells to a wall ("w")
                self.grid[y][x] = "w" 
 


#The method which generates a maze using prims algorithm
    def Prims(self):
        self.createMaze()
    #An array of the coordinates of the possible cells that could be turned into paths, Tuples are used to store the coordinates as individual items
        frontierCells = [] 

        #Picks the a random Y coordinates within the confines of the walls ("w")
        StartRow = random.randint(2,48) 

        #Picks the a random X coordinates within the confines of the walls ("w")
        StartCollumn = random.randint(2,48)

        #Sets the randomly pick coordinates as a path ("P")
        self.grid[StartRow][StartCollumn] = "P"

        #From the starting point the cells around it are selected as frontier cells

        #Start of the first frontier cell check
        #Looks at west of the starting point by 1 cell
        #if the cell it's looking at is wall ("w") and not a barrier ("b") then that cell's coordinates get appended a tuple in frontierCells
        if self.grid[StartRow-1][StartCollumn] != "b" and self.grid[StartRow-1][StartCollumn] == "w":
            frontierCells.append((StartRow-1,StartCollumn))

        #Looks east of the starting point by 1 cell
        #if the cell it's looking at is wall ("w") and not a barrier ("b") then that cell's coordinates get appended as a tuple in frontierCells
        if self.grid[StartRow+1][StartCollumn] != "b" and self.grid[StartRow+1][StartCollumn] == "w":
            frontierCells.append((StartRow+1,StartCollumn))

        # Looks south of the starting point by 1 cell
        #if the cell it's looking at is wall ("w") and not a barrier ("b") then that cell's coordinates get appended as a tuple in frontierCells
        if self.grid[StartRow][StartCollumn-1] != "b" and self.grid[StartRow][StartCollumn-1] == "w": 
            frontierCells.append((StartRow,StartCollumn-1))

        #Looks north of the starting point by 1 cell
        #if the cell it's looking at is wall ("w") and not a barrier ("b") then that cell's coordinates get appended as a tuple in frontierCells
        if self.grid[StartRow][StartCollumn+1] != "b" and self.grid[StartRow][StartCollumn+1] == "w": 
            frontierCells.append((StartRow,StartCollumn+1))

        
            
        #This WHILE loop will run until the maze has been fully generated
        while len(frontierCells) > 0:

            #The next frontier cell is randomly selected from frontierCell, the tuple pair of cooridnates gets stored in nextFrontierCell
            nextFrontierCell = random.randint(0,len(frontierCells)-1)

            #first item in the tuple pair (the Y cooridnate) is stored in NextRow
            NextRow = frontierCells[nextFrontierCell][0]
            #second item in the tuple pair (the X cooridnate) is stored in NextCollumn
            NextCollumn = frontierCells[nextFrontierCell][1] 
        
            #Sets the chosen frontier cell to a path ("P")
            self.grid[NextRow][NextCollumn] = "P"

            #removes the frontier cell from the array which was chosen to be the next path cell
            frontierCells.pop(nextFrontierCell) 

            #The cells around the chosen path cell are checked for new frontier cells to be added to the array frontierCells

            #Start of the frontier cell check
            #Looks west if the chosen path cell by 1 cell
            #if the cell it's looking at is wall("w) and not a path ("P") then that cell's coordinates get appended as a tuple in frontierCells
            if self.grid[NextRow-1][NextCollumn] != "P" and self.grid[NextRow-1][NextCollumn] == "w": 
                frontierCells.append((NextRow-1,NextCollumn))

            #Looks east of the chosen path cell by 1 cell
            #if the cell it's looking at is wall ("w") and not a path ("P")then that cell's coordinates get appended as a tuple in frontierCells
            if self.grid[NextRow+1][NextCollumn] != "P" and self.grid[NextRow+1][NextCollumn] == "w": 
                frontierCells.append((NextRow+1,NextCollumn))

            #Looks south of the chosen path cellby 1 cell
            #if the cell it's looking at is wall ("w") and not a path ("P") then that cell's coordinates get appended as a tuple in frontierCells
            if self.grid[NextRow][NextCollumn-1] != "P" and self.grid[NextRow][NextCollumn-1] == "w": 
                frontierCells.append((NextRow,NextCollumn-1))

            #Looks north of the chosen path cell by 1 cell
            #if the cell it's looking at is wall ("w") and not a path ("P") then that cell's coordinates get appended as a tuple in frontierCells
            if self.grid[NextRow][NextCollumn+1] != "P" and self.grid[NextRow][NextCollumn+1] == "w":
                frontierCells.append((NextRow,NextCollumn+1))
            #End of the frontier cell check

            #This FOR loop will prune any frointer cells with a check count greater than two
            #The CheckCount is increased by one each time the frontier cell has a path or barrier infront of it.
            #The FOR loop iterates backwards to avoid an index error
            for i in range(len(frontierCells)-1,-1,-1):

                #first item in the tuple pair (the Y cooridnate) from the frontier cell being checked is stored CheckRow
                CheckRow = frontierCells[i][0]

                #second item in the tuple pair (the x cooridnate) from the frontier cell being checked is stored CheckCollumn
                CheckCollumn = frontierCells[i][1]

                CheckCount = 0

                #Start of the prune check
                #Looks west of the frontier cell being checked by 1 cell
                if self.grid[CheckRow-1][CheckCollumn] == "b" or self.grid[CheckRow-1][CheckCollumn] == "P":
                    CheckCount = CheckCount + 1

                #Looks east of the frontier cell being checked by 1 cell
                if self.grid[CheckRow+1][CheckCollumn] == "b" or self.grid[CheckRow+1][CheckCollumn] == "P":
                    CheckCount = CheckCount + 1

                #Looks south of the frontier cell being checked by 1 cell
                if self.grid[CheckRow][CheckCollumn-1] == "b" or self.grid[CheckRow][CheckCollumn-1] == "P":
                    CheckCount = CheckCount + 1

                #Looks north of the frontier cell being checked by 1 cell
                if self.grid[CheckRow][CheckCollumn+1] == "b" or self.grid[CheckRow][CheckCollumn+1] == "P":
                    CheckCount = CheckCount + 1
                #End of the prune check


                #The frontier cell is pruned in which it's tuple pair of coordinates are removed from the array
                if CheckCount >= 2:
                    frontierCells.pop(i) 

        #returns the 2d array stored in grid which will be used to draw out the maze using Tkinter in DrawMaze.py
        return self.grid 
 
                


