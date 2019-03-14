# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:36:55 2019

@author: m_taran
"""

import Grid as Grid

class Node:
    
    def __init__(self, playerHandSize, opponentHandSize, pType, oType, board = None, targetDepth = 1):
        self.command = ""
        self.playerType = pType
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
        temp = Node(self.minplayerHandSize, self.maxplayerHandSize-1, self.opponentType, self.playerType, self.gameBoard, self.depth-1)
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
                self.branches[-1].buildChildNodes()
    
    def calculateHeuristic(self):
        rowValue = {"1":0,"2":10,"3":20,"4":30,"5":40,"6":50,"7":60,"8":70,"9":80,"10":90,"11":100,"12":110}
        columnValue = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
        
        total = 0
        
        temp = self.gameBoard.board
        
        for row in temp:
            for column in temp[row]:
                
                if(temp[row][column].dot == 1):
                    if(temp[row][column].color == 1):
                        #White Empty
                        total+=rowValue[row]+columnValue[column]
                    else:
                        #Red Empty
                        total+=-1.5*(rowValue[row]+columnValue[column])
                elif(temp[row][column].dot == 2):
                    if(temp[row][column].color == 1):
                        #White Full
                        total+=3*(rowValue[row]+columnValue[column])
                    else:
                        #Red Full
                        total+=-2*(rowValue[row]+columnValue[column])
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
        self.getBestMove((self.playerType == 0), True)
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