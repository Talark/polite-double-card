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
        self.msg = ""
        #lastMove contains the command from the last move
        self.lastMove = "None"
        #currentPlayer should switch from 1 to 0 and back, this lets it be used as a conditional
        self.currentPlayer = 0
        #board is a dictionary of dictionaries where A1 is the bottom left of the board
        #letters denote columns and numbers denote rows
        self.board = {
                "12": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "11": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "10": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "9": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "8": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "7": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },                        
                "6": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },   
                "5": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },  
                "4": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "3": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "2": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
                            },
                "1": {
                        "A": HalfCard.HalfCard(0,0,""),
                        "B": HalfCard.HalfCard(0,0,""),
                        "C": HalfCard.HalfCard(0,0,""),
                        "D": HalfCard.HalfCard(0,0,""),
                        "E": HalfCard.HalfCard(0,0,""),
                        "F": HalfCard.HalfCard(0,0,""),
                        "G": HalfCard.HalfCard(0,0,""),
                        "H": HalfCard.HalfCard(0,0,""),                    
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
        
    def copyGrid(self, board):
        self.msg = board.msg
        self.currentPlayer = board.currentPlayer
        self.lastMove = board.lastMove
        
        temp = board.board
        
        for row in self.board:
            for column in self.board[row]:
                self.board[row][column].dot = temp[row][column].dot
                self.board[row][column].color = temp[row][column].color
                self.board[row][column].neighbor = temp[row][column].neighbor
        
    
    #We need to change the input string to a list
    def inputToList(self, inputString): 
        command = inputString.split()
        return command
    
    #This method assumes the command is properly formated. DO NOT USE AS A PUBLIC METHOD 
    def __setCard__(self, commandFormated):
        neighborCoordinates = self.otherHalfCoordinates(commandFormated[1], commandFormated[2], commandFormated[3])
        firstHalfInfo = self.cardInfo[commandFormated[1]]
        secondHalfInfo= self.otherHalfInfo(firstHalfInfo)
            
        originCoords = commandFormated[2]+" "+commandFormated[3]
        neighCoords = neighborCoordinates[0]+" "+neighborCoordinates[1]
            
        #PROOF CHECK THIS
        self.board[commandFormated[3]][commandFormated[2]].setValues(firstHalfInfo[0],firstHalfInfo[1],neighCoords)
        self.board[neighborCoordinates[1]][neighborCoordinates[0]].setValues(secondHalfInfo[0],secondHalfInfo[1],originCoords)
    
    #should only set appropriate cells of grid is move is legal
    #must return false if not legal, true otherwise
    def playCard(self, command):
        commandFormated = self.inputToList(command)
        self.msg+="Putting "+command+" in grid if legal\n"
        
        isLegal = self.moveIsLegal(commandFormated)
        if(isLegal):
            #First half piece refers to the coordinate that we received, while second half piece is the coordinate of the piece
            #that we interpolated from the orientation
            if(commandFormated[0] == "0"):
                self.__setCard__(commandFormated)
            else:
                #Legality of move already confirmed, no need to check again
                self.recycleAndPlayCard(commandFormated)
                
            self.lastMove = command
            return True
        else:
            return(False)
    
    #same as above, but has an additional legality check (ensure command targets 2 halves of 1 piece and piece is not under others)
    #can modify recycle command into a play command afterwards (just an implementation option if you want to do it that way)
    def recycleAndPlayCard(self, commandFormatted):
        self.msg+="Modifying grid for recycle, then playing card\n"
        #Remove old card
        
        self.board[commandFormatted[1]][commandFormatted[0]].setValues(0,0,"")
        self.board[commandFormatted[3]][commandFormatted[2]].setValues(0,0,"")
        
        #Removing uneeded info
        commandFormatted = commandFormatted[4:]
        commandFormatted.insert(0,'0')
        
        #Place new card
        self.__setCard__(commandFormatted)
    
    #Determine if move is legal and returns true or false
    #Input is list of 3 1) is orientation, 2-3)

    def moveIsLegal(self,commandFormatted):
       
        #Regular move legality check
        if(commandFormatted[0] == "0"): 
            if (int(commandFormatted[1]) < 1 or int(commandFormatted[1]) > 8):
                self.msg+="Rotation was out of bounds of the dictionnary for cardInfo\n"
                return False
            for element in commandFormatted: 
                if(int(commandFormatted[3])<1 or int(commandFormatted[3])>12):
                    self.msg+="Row index was out of bounds of the dictionnary for cardInfo\n"
                    return False
                if(commandFormatted[2]<'A' or commandFormatted[2]>'H'):
                    self.msg+="Column index was out of bounds of the dictionnary for cardInfo\n"
                    return False
            if(self.spaceAvailable(commandFormatted[2],commandFormatted[3]) == False):
                self.msg+="Targeted location does not meet playable criteria\n"
                return False
            #Checked Bottom Left Space
            if(int(commandFormatted[1]) % 2 == 1):
                #Checks space next to Bottom Left
                if(commandFormatted[2] == "H"):
                    self.msg+="Targeted location does not meet playable criteria\n"
                    return False
                if(self.spaceAvailable(chr(ord(commandFormatted[2]) + 1),commandFormatted[3]) == False):
                    self.msg+="Targeted location does not meet playable criteria\n"
                    return False
            else:
                if(commandFormatted[3] == "12"):
                    self.msg+="Targeted location does not meet playable criteria\n"
                    return False
        #Recycling move legality check
        else:
            #Check both targets are of same card
            for element in commandFormatted: 
                if(int(commandFormatted[6])<1 or int(commandFormatted[6])>12):
                    self.msg+="Row index was out of bounds of the dictionnary for cardInfo\n"
                    return False
                if(commandFormatted[5]<'A' or commandFormatted[5]>'H'):
                    return False
                if(int(commandFormatted[1])<1 or int(commandFormatted[1])>12):
                    self.msg+="Row index was out of bounds of the dictionnary for cardInfo\n"
                    return False
                if(commandFormatted[0]<'A' or commandFormatted[0]>'H'):
                    return False
                if(int(commandFormatted[3])<1 or int(commandFormatted[3])>12):
                    self.msg+="Row index was out of bounds of the dictionnary for cardInfo\n"
                    return False
                if(commandFormatted[2]<'A' or commandFormatted[2]>'H'):
                    self.msg+="Column index was out of bounds of the dictionnary for cardInfo\n"
                    return False
                if(int(commandFormatted[4])<1 or int(commandFormatted[4])>8):
                    self.msg+="Rotation was out of bounds of the dictionnary for cardInfo\n"
                    return False
            if(not self.isOtherHalf(commandFormatted[0],commandFormatted[1],commandFormatted[2],commandFormatted[3])): 
                self.msg+="Halves chosen for recycling are not part of the same card\n"
                return False
            
            #Check that target for removal was not last played
            temp = self.lastMove.split()
            keyNumber = temp[-1]
            keyLetter = temp[-2]
            
            if(commandFormatted[0] == keyLetter and commandFormatted[1] == keyNumber):
                self.msg+="Card selected for recycling was the last card played\n"
                return False
            if(commandFormatted[2] == keyLetter and commandFormatted[3] == keyNumber):
                self.msg+="Card selected for recycling was the last card played\n"
                return False
            
            #Check that removal is legal
            if(commandFormatted[0]==commandFormatted[2]):
                #Check that nothing exists above card in one column
                if(int(commandFormatted[1]) < int(commandFormatted[3])):
                    maxVar = int(commandFormatted[3])
                else: 
                    maxVar = int(commandFormatted[1])
                if(maxVar+1 > 12): 
                    return True
                if(self.spaceAvailable(commandFormatted[2],str(maxVar+1)) == False):
                    self.msg+="Selected card has other cards on top. Cannot remove\n"
                    return False
            else:
                #Check that nothing exists above card in 2 columns
                if(int(commandFormatted[3])+1 > 12): 
                    if(self.spaceAvailable(commandFormatted[2],str(int(commandFormatted[3])+1)) == False):
                        self.msg+="Selected card has other cards on top. Cannot remove\n"
                        return False
                    if(self.spaceAvailable(commandFormatted[0],str(int(commandFormatted[1])+1)) == False):
                        self.msg+="Selected card has other cards on top. Cannot remove\n"
                        return False
            
            #Extract last 3 values in recycle command
            temp = commandFormatted[4:]
            #Add a 0 to treat it as regular move
            temp.insert(0,'0')
            if(not self.moveIsLegal(temp)): 
                self.msg+="Recycling could not be performed\n"
                return False
            
        return True 
    #Checks if the space is available and the space below is taken
    def spaceAvailable(self,indexLetter, indexNum):
        if(int(indexNum) > 1):
            if(int(indexNum)>12):
                return False
            return(self.board[indexNum][indexLetter].color == 0 and self.board[str(int(indexNum)-1)][indexLetter].color != 0 )
        else: 
            return(self.board[indexNum][indexLetter].color == 0) 
     
            #Check state and state next to it
    def isOtherHalf(self,indexLetter1, indexNum1,indexLetter2, indexNum2):
        #NEED TO DOUBLE CHECK THAT THIS WORKS
        temp = self.board[indexNum2][indexLetter2].neighbor.split()
        return(len(temp) == 2 and temp[0] == indexLetter1 and temp[1] == indexNum1)
        
       #Method for finding the coordinates of the other half of a tile.
    #Returns a list with [Character,Number] values
    #HELPER
    def otherHalfCoordinates(self,orientation, indexLetter, indexNumber):
        if(int(orientation) % 2 == 1):
            indexLetter = chr(ord(indexLetter) + 1)            
        else:
            indexNumber = str(int(indexNumber) + 1)
        return([indexLetter, indexNumber])
        
    #Type list needs to be card info with first part being 
    def otherHalfInfo(self,cardinfo):
        return(-1*np.subtract(cardinfo,[3,3]))
        
        
    #This method should receive coordinates from which it needs to radiate out from to check for a win
    #In general this method must check for wins from 2 origin points since cards have 2 halves that can be part of a 4-set
    def checkForWin(self, command):
        #Get number and letter indeces of origin and neighbor
        commandFormatted = self.inputToList(command)
        oNum = commandFormatted[-1]
        oLet = commandFormatted[-2]
        nNum = oNum
        nLet = oLet
        if(int(commandFormatted[-3]) % 2 == 1):
            nLet = chr(ord(nLet)+1)
        else:
            nNum = str(int(nNum)+1)
        
        colorWin = 0
        dotWin = 0
        
        #Check for wins at origin
        
        #Check horizontal
        winTemp = self.checkWinAlongOffsets(oNum,oLet,1,0)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
        
        #Check vertical
        winTemp = self.checkWinAlongOffsets(oNum,oLet,0,1)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
        
        #Check diag (\)
        winTemp = self.checkWinAlongOffsets(oNum,oLet,1,-1)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
        
        #Check diag (/)
        winTemp = self.checkWinAlongOffsets(oNum,oLet,1,1)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
            
        #Check for wins at neighbor
        
        #Check horizontal
        winTemp = self.checkWinAlongOffsets(nNum,nLet,1,0)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
        
        #Check vertical
        winTemp = self.checkWinAlongOffsets(nNum,nLet,0,1)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
            
        #Check diag (\)
        winTemp = self.checkWinAlongOffsets(nNum,nLet,1,-1)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
        
        #Check diag (/)
        winTemp = self.checkWinAlongOffsets(nNum,nLet,1,1)
        if(winTemp[0]>=4):
            colorWin+=1
        if(winTemp[1]>=4):
            dotWin+=1
        
        #Print congrats message and return true if winning sets found
        if(dotWin>0 and colorWin>0):
            if(self.currentPlayer == 0):
                self.msg+="Both colors and dots have winning set. Current player colors wins the game.\n"
            else:
                self.msg+="Both colors and dots have winning set. Current player dots wins the game.\n"
            return True
        
        if(dotWin>0):
            self.msg+="Dots have made a set of 4. Dots Win.\n"
            return True
             
        if(colorWin>0):
            self.msg+="Colors have made a set of 4. Colors Win.\n"
            return True
        
        #Return False if no winning sets found
        return False
        
    def checkWinAlongOffsets(self,number,letter,letOffset,numOffset):
        #Initialise counts and types
        colorType = self.board[number][letter].color
        dotType = self.board[number][letter].dot
        colorCount = 1
        dotCount = 1
        
        checkDot = True
        checkColor = True
        
        #Check cells in positive offset range
        for i in range(3):
            #Next cell to check
            iNum = str(int(number)+(i+1)*numOffset)
            iLet = chr(ord(letter)+(i+1)*letOffset)
            
            #If out of bounds, break
            if(int(iNum)<1 or int(iNum)>12):
                break
            if(iLet<'A' or iLet>'H'):
                break
            
            #If next cell empty, break
            if(self.board[iNum][iLet].color == 0):
                break
                
            #Compare values unless different one seen previouly
            if(checkColor and self.board[iNum][iLet].color == colorType):
                colorCount+=1
            else:
                checkColor = False
                
            if(checkDot and self.board[iNum][iLet].dot == dotType):
                dotCount+=1
            else:
                checkDot = False
        
        checkDot = True
        checkColor = True
        
        #Check cells in negative offset range
        for i in range(3):
            #Next cell to check
            iNum = str(int(number)-(i+1)*numOffset)
            iLet = chr(ord(letter)-(i+1)*letOffset)
            
            #If out of bounds, break
            if(int(iNum)<1 or int(iNum)>12):
                break
            if(iLet<'A' or iLet>'H'):
                break
                
            #If next cell empty, break
            if(self.board[iNum][iLet].color == 0):
                break
            
            #Compare values unless different one seen previouly
            if(checkColor and self.board[iNum][iLet].color == colorType):
                colorCount+=1
            else:
                checkColor = False
                
            if(checkDot and self.board[iNum][iLet].dot == dotType):
                dotCount+=1
            else:
                checkDot = False
                
        return ([colorCount,dotCount])
    
    #Figure this might be usefull later on for AI implementation since dictionary accessing with indeces can get messy code wise
    def toList(self):
        print("Here's the grid as a list")
    
    #Self explanatory
    #INPROGRESS
    def display(self):
        s = ""
        for row in self.board:
            s = s + row + ""
            for column in self.board[row]:
                s = s + "\t" + str(self.board[row][column])
            s = s + "\n"
        s = s + "\t"
        for row in self.board["1"]:
             s = s + row + "\t"
        print(s)
        
    #Print contents of msg and purge contents
    def printMsgBuffer(self):
        print(self.msg)
        self.msg = ""
