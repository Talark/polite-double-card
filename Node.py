# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:36:55 2019

@author: m_taran
"""

import Grid as Grid
import random

class Node:
    
    def __init__(self, playerHandSize, opponentHandSize, ai, pType, oType, board = None, targetDepth = 1):
        self.command = ""
        self.playerType = pType
        self.aiType = ai
        self.opponentType = oType
        self.gameBoard = Grid.Grid()
        
        if(board != None):
            self.gameBoard.copyGrid(board)
            
        #this makes an empty list
        self.branches = []
        
        if(targetDepth<0):
            self.depth = 0
        else:
            self.depth = targetDepth
            
        self.score = "None"
        self.maxplayerHandSize = playerHandSize
        self.minplayerHandSize = opponentHandSize
        
    #ideal to check command for legality before creating a node
    #this would eliminate illegal moves from ever being chosen
    def createNodeBranch(self, command):
        temp = Node(self.minplayerHandSize, self.maxplayerHandSize-1, self.aiType, self.opponentType, self.playerType, self.gameBoard, self.depth-1)
        temp.command = command
        temp.gameBoard.playCard(command)
        self.branches.append(temp)
    
    #This method should call GenerateLegalMoves, then iterate through the list of commands
    #and finally call createNodeBranch based on the command.
    #After each node is built, buildChildNodes should be called on the new node once again if self.depth > 1
    #An else statement can be included to immediately calculate the heuristic score of the leaf nodes once they are reached
    def buildChildNodes(self):
        #Generate legal moves for root
        moveList = self.__GenerateLegalMoves__()
        
        #For every legal move createNodeBranch
        for move in moveList:
            self.createNodeBranch(move)
            # and build child nodes if max depth not reached
            if(self.branches[-1].depth == 0):
                self.branches[-1].calculateHeuristic()
            #Otherwise calculate score of current game state
            else:
                #Check that new node does not result in end of game
                if(not self.gameBoard.checkForWin(move)):
                    self.branches[-1].buildChildNodes()
                else:
                    self.branches[-1].calculateHeuristic()
        
        random.shuffle(self.branches)
    
    def calculateHeuristic(self):
        #Using command along with checkAlongOffset
        #We can determine how beneficial a given move is
        
        total = 0
        
        temp = [0,0]
        color3Float = False
        dot3Float = False
        
        result = self.checkResult(self.command)
        for line in result:
            #Base value of
            #4
            if(line[0]>=4):
                temp[0] = 1000
            #3
            elif(line[0]==3):
                if(min(line[1],line[2])>=1):
                    temp[0] = 500
                elif(max(line[1],line[2])>=1):
                    if(temp[0]<100):
                        temp[0] = max(temp[0],50)
                        color3Float = True
                    elif(color3Float):
                        temp[0]=1000
            #2
            elif(line[0]==2 and min(line[1],line[2])>=2):
                temp[0] = max(temp[0],10)
            #1
            elif(line[0]==1 and min(line[1],line[2])>=3):
                temp[0] = max(temp[0],1)
            
            #Base value of
            #4
            if(line[3]>=4):
                temp[1] = 1000
            #3
            elif(line[3]==3):
                if(min(line[4],line[5])>=1):
                    temp[1] = 500
                elif(max(line[4],line[5])>=1):
                    if(temp[1]<100):
                        temp[1] = max(temp[1],50)
                        dot3Float = True
                    elif(dot3Float):
                        temp[1]=1000
            #2
            elif(line[3]==2 and min(line[4],line[5])>=2):
                temp[1] = max(temp[1],10)
            #1
            elif(line[3]==1 and min(line[4],line[5])>=3):
                temp[1] = max(temp[1],1)
            
    
        total = temp[self.aiType] - temp[1-self.aiType]
        
        
        #Wrapped open values
        
        self.score = total
    
    #This method should always be called on the root node first, otherwise not all moves are considered
    #Once called, a depth first search must be performed where the highest score and the command of the node is returned
    #as a list ex: [int score, String command]. On first call, maxScore should use default value and should swap its value on
    #every recursive call. When maxScore is True, scores should be compared as is, when false the scores should be multiplied by -1
    #This allows the opponent to minimize our score
    def getBestMove(self, maxScore = True, root = False):
        if(self.depth>0):
            for possibility in self.branches:
                temp = possibility.getBestMove(not maxScore)
                if(self.score == "None"):
                    best = possibility.command
                    self.score = temp
                elif(maxScore):
                    if(self.score < temp):
                        best = possibility.command
                        self.score = temp
                else:
                    if(self.score > temp):
                        best = possibility.command
                        self.score = temp
                        
        if(root):
            self.command = best
        
        return self.score
                    
    def makeMove(self):
        self.getBestMove(True, True)
        return self.command
    
    def countLeaves(self):
        total = 0
        
        if(self.depth==1):
            return len(self.branches)
        
        for node in self.branches:
            total+=node.countLeaves()
        
        return total
                
    
    #This method returns a list of commands that are all possible legal moves for the given grid
    def __GenerateLegalMoves__(self):
        legalMoveList = []
        
        board = self.gameBoard.board
        
        #This nested loop adds all legal regular moves
        if(self.maxplayerHandSize>0):
            for row in board:
                command = ["0","","",row]
                for column in board[row]:
                    command[2] = column
                    for i in range(8):
                        command[1] = str(i+1)
                        if(self.gameBoard.moveIsLegal(command)):
                            legalMoveList.append(' '.join(command))
                            
        #This nested loop generates all legal recycling moves            
        else:
            #Make a list of all possible targets for recycling
            
            checkedColumns = {"A":False,"B":False,"C":False,"D":False,"E":False,"F":False,"G":False,"H":False}
            
            possibleRecyclingTargets = []
            
            for row in board:
                for column in board[row]:
                    if((not checkedColumns[column]) and board[row][column].dot!=0):
                        checkedColumns[column] = True
                        #This line ensures that horizontal cards do not appear in the list twice
                        checkedColumns[board[row][column].neighbor.split()[0]] = True
                        possibleRecyclingTargets.append(column+" "+row+" "+board[row][column].neighbor)
            
            #For every target repeat above for all possible moves
            for target in possibleRecyclingTargets:
                for row in board:
                    temp = target.split()
                    command = [temp[0],temp[1],temp[2], temp[3],"","",row]
                    for column in board[row]:
                        command[-2] = column
                        for i in range(8):
                            command[-3] = str(i+1)
                            if(self.gameBoard.moveIsLegal(command)):
                                legalMoveList.append(' '.join(command))
        
        return legalMoveList
    
    #The following are helper methods for the heuristic
    #Return highest potential for colors and dots to win as numerical value
    def checkResult(self, command):
        #Get number and letter indeces of origin and neighbor
        commandFormatted = command.split()
        oNum = commandFormatted[-1]
        oLet = commandFormatted[-2]
        nNum = oNum
        nLet = oLet
        if(int(commandFormatted[-3]) % 2 == 1):
            nLet = chr(ord(nLet)+1)
        else:
            nNum = str(int(nNum)+1)
        
        temp = []
        
        #Check for wins at origin
        
        #Check horizontal
        temp.append(self.checkAlongOffsets(oNum,oLet,1,0))
        
        
        #Check vertical
        temp.append(self.checkAlongOffsets(oNum,oLet,0,1))
        
        
        #Check diag (\)
        temp.append(self.checkAlongOffsets(oNum,oLet,1,-1))
        
        
        #Check diag (/)
        temp.append(self.checkAlongOffsets(oNum,oLet,1,1))
        
            
        #Check for wins at neighbor
        
        #Check horizontal
        temp.append(self.checkAlongOffsets(nNum,nLet,1,0))
        
        
        #Check vertical
        temp.append(self.checkAlongOffsets(nNum,nLet,0,1))
        
            
        #Check diag (\)
        temp.append(self.checkAlongOffsets(nNum,nLet,1,-1))
        
        
        #Check diag (/)
        temp.append(self.checkAlongOffsets(nNum,nLet,1,1))
        
        
        return temp
        
    def checkAlongOffsets(self,number,letter,letOffset,numOffset):
         #Initialise counts and types
        board = self.gameBoard.board
        colorType = board[number][letter].color
        dotType = board[number][letter].dot
        colorCount = 1
        dotCount = 1
        openLeft = 0
        openRight = 0
        dotBlockLeft = 3
        dotBlockRight = 3
        colorBlockLeft = 3
        colorBlockRight = 3
        
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
            if(board[iNum][iLet].color == 0):
                if(self.gameBoard.spaceAvailable(iLet,iNum)):
                    openRight+=1
                
            #Compare values unless different one seen previouly
            if(checkColor and board[iNum][iLet].color == colorType):
                colorCount+=1
            else:
                if(board[iNum][iLet].color != 0):
                    colorBlockRight = openRight
                checkColor = False
                
            if(checkDot and board[iNum][iLet].dot == dotType):
                dotCount+=1
            else:
                if(board[iNum][iLet].dot != 0):
                    dotBlockRight = openRight
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
            if(board[iNum][iLet].color == 0):
                if(self.gameBoard.spaceAvailable(iLet,iNum)):
                    openLeft+=1
            
            #Compare values unless different one seen previouly
            if(checkColor and board[iNum][iLet].color == colorType):
                colorCount+=1
            else:
                if(board[iNum][iLet].color != 0):
                    colorBlockLeft = openLeft
                checkColor = False
                
            if(checkDot and board[iNum][iLet].dot == dotType):
                dotCount+=1
            else:
                if(board[iNum][iLet].dot != 0):
                    dotBlockLeft = openLeft
                checkDot = False
                
        return ([colorCount,min(colorBlockLeft, openLeft),min(colorBlockRight,openRight),dotCount,min(dotBlockLeft,openLeft),min(dotBlockRight,openRight)])