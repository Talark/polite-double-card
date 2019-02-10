# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:45:55 2019

@author: m_taran
"""
#Feel free to add methods as needed

import HalfCard as HalfCard
import numpy as np

class Grid:
    
    def __init__(self):
        #lastMove contains the command from the last move
        self.lastMove = "None"
        #currentPlayer should switch from 1 to 0 and back, this lets it be used as a conditional
        self.currentPlayer = 1
        #board is a dictionary of dictionaries where A1 is the bottom left of the board
        #letters denote columns and numbers denote rows
        self.board = {
                "A": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "B": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "C": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "D": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "E": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "F": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "G": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "H": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            }
                }
        #Used for looking up based on orientation
        #Returns [Color,Dot]
        self.cardInfo = {
                "1": [2,2],
                "2": [1,1],
                "3": [1,1],
                "4": [2,2],
                "5": [2,1],
                "6": [1,2],
                "7": [1,2],
                "8": [2,1]
                }
        
    #We need to change the input string to a list
    def inputToList(self, inputString): 
        inputString = "A B C D"
        command = inputString.split()
        return command
    
    #should only set appropriate cells of grid is move is legal
    #must return false if not legal, true otherwise
    def playCard(self, command):
        commandFormated = self.inputToList(command)
        print("Putting",command,"in grid if legal")
        isLegal = self.moveIsLegal(commandFormated)
        if(isLegal):
            return(True)
            #First half piece refers to the coordinate that we received, while second half piece is the coordinate of the piece
            #that we interpolated from the orientation
            firstHalfPieceChar =commandFormated[2]
            firstHalfPieceNum = commandFormated[3]
            orientation = commandFormated[1]
            neighborCoordinates = self.otherHalfCoordinates(orientation, firstHalfPieceChar, firstHalfPieceNum)
            secondHalfPieceChar = neighborCoordinates[0]
            secondHalfPieceNum = neighborCoordinates[1]
            firstHalfInfo = self.cardInfo[orientation]
            secondHalfInfo= self.otherHalfInfo(firstHalfInfo)
            #PROOF CHECK THIS
            self.board[firstHalfPieceChar][firstHalfPieceNum].setValues(firstHalfInfo[0],firstHalfInfo[1],"")
            self.board[secondHalfPieceChar][secondHalfPieceNum].setValues(secondHalfInfo[0],secondHalfInfo[1],"")            
        else:
            return(False)
    
    #same as above, but has an additional legality check (ensure command targets 2 halves of 1 piece and piece is not under others)
    #can modify recycle command into a play command afterwards (just an implementation option if you want to do it that way)
    def recycleAndPlayCard(self, command):
        print("Modifying grid and command for recycle if legal")
    
    #Determine if move is legal and returns true or false
    #Input is list of 3 1) is orientation, 2-3)

    def moveIsLegal(self,commandFormatted):
        if(commandFormatted[0] == "0"):    
            if(self.spaceAvailable(commandFormatted[2],commandFormatted[3]) == False): return False
            #Checked Bottom Left Space
            if(int(commandFormatted[1]) % 2 == 1):
                #Checks space next to Bottom Left
                if(self.spaceAvailable(chr(ord(commandFormatted[2]) + 1),commandFormatted[3]) == False): return False
        else:
            if(not self.moveIsLegal(commandFormatted[5:])): return False
            if(not self.isOtherHalf(commandFormatted[0],commandFormatted[1],commandFormatted[2],commandFormatted[3])): return False
        return True 
    #Checks if the space is available and the space below is taken
    def spaceAvailable(self,indexLetter, indexNum):
        if(indexNum > 1):
            return(self.board[indexLetter][indexNum].color != 0 and self.board[indexLetter][indexNum-1].color != 0 )
        else: 
            return(self.board[indexLetter][indexNum].color != 0) 
     
            #Check state and state next to it
    def isOtherHalf(self,indexLetter1, indexNum1,indexLetter2, indexNum2):
        #NEED TO DOUBLE CHECK THAT THIS WORKS
        return( self.board[indexLetter1][indexNum1] == self.board[indexLetter2][indexNum2].neighbor)
                       
        print("Checking if move is legal")
        
       #Method for finding the coordinates of the other half of a tile.
    #Returns a list with [Character,Number] values
    #HELPER
    def otherHalfCoordinates(self,orientation, indexLetter, indexNumber):
        if(int(orientation) % 2 == 1):
            indexLetterNeighbor = chr(ord(indexLetter) + 1)
            indexNumberNeighbor = indexNumber
        else:
            indexLetterNeighbor = indexLetter
            indexNumberNeighbor = chr(ord(indexNumber) + 1)
        return([indexLetterNeighbor, indexNumberNeighbor])
        
    #Type list needs to be card info with first part being 
    def ohterHalfInfo(self,cardinfo):
        return(-1*np.subtract(cardinfo,[3,3]))
        
        
    #This method should receive coordinates from which it needs to radiate out from to check for a win
    #In general this method must check for wins from 2 origin points since cards have 2 halves that can be part of a 4-set
    def checkForWin(self, command):
        print("Checking for wins originating from command location")
    
    #Figure this might be usefull later on for AI implementation since dictionary accessing with indeces can get messy code wise
    def toList(self):
        print("Here's the grid as a list")
    
    #Self explanatory
    #INPROGRESS
    def display(self):
        s = ""
        for row in self.board:
            s = s + row + " "
            for column in self.board[row]:
                s = s + str(self.board[row][column])
            s = s + "\n"
        s = s + " "
        for row in self.board["A"]:
             s = s + row + ""
        print(s)
        print("*throws board in face*")

