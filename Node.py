# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:36:55 2019

@author: m_taran
"""

import Grid as Grid

class Node:
    
    def __init__(self, playerHandSize, opponentHandSize, pType, oType, board = None, targetDepth = 1):
        self.command = ""
        self.playType = pType
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
            
        self.score = 0
        self.maxplayerHandSize = playerHandSize
        self.minplayerHandSize = opponentHandSize
        
    #ideal to check command for legality before creating a node
    #this would eliminate illegal moves from ever being chosen
    def createNodeBranch(self, command):
        temp = Node(self.minplayerHandSize, self.maxplayerHandSize-1, self.opponentType, self.playerType, self.board, self.depth-1)
        temp.command = command
        temp.gameBoard.playCard(command)
        self.branches.append(temp)
    
    #This method should call GenerateLegalMoves, then iterate through the list of commands
    #and finally call createNodeBranch based on the command.
    #After each node is built, buildChildNodes should be called on the new node once again if self.depth > 1
    #An else statement can be included to immediately calculate the heuristic score of the leaf nodes once they are reached
    def buildChildNodes(self):
        print("buildChildNodes not implemented yet")
    
    def calculateHeuristic(self, targetNode):
        #This just ensures non node types are handled
        if(not type(targetNode).__name__=="Node"):
            return 0
        print("calculateHeuristic not implemented yet")
    
    #This method should always be called on the root node first, otherwise not all moves are considered
    #Once called, a depth first search must be performed where the highest score and the command of the node is returned
    #as a list ex: [int score, String command]. On first call, maxScore should use default value and should swap its value on
    #every recursive call. When maxScore is True, scores should be compared as is, when false the scores should be multiplied by -1
    #This allows the opponent to minimize our score
    def getBestMove(self, maxScore = True):
        print("getBestMove not implemented yet")
    
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