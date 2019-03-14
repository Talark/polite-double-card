# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:32:20 2019

@author: m_taran
"""

import Player as Player
import Grid as Grid
import Node as Node
import random

class AI(Player.Player):
    
    def __init__(self, value=False):
        super(AI,self).__init__()
        self.depth = 1
        
        temp = bool(value)
        if(value == True):
            self.traceMode = True
        #This ensures that default mode keeps trace off
        elif(temp == True):
            self.traceMode = False
        else:
            self.traceMode = False
            
        self.traceBuffer = []
        
    def setDepth(self, value : int):
        self.depth = value
    
    def turnStart(self, board : Grid.Grid, opponentHand = 0):
        if(self.hand>0):
            self.playFromHand(board, opponentHand)
        else:
            self.recycleAndPlay(board, opponentHand)
        
        nody = Node.Node(self.hand,opponentHand,self.playType,1-self.playType,board, self.depth)

        nody.buildChildNodes()

        nody.makeMove()
        
        if(self.traceMode):
            self.storeTrace(nody)
            
        return nody.command
    
    def playFromHand(self, board : Grid.Grid, opponentHand = 0):
        print("Playing from hand")
        
        
    def recycleAndPlay(self, board : Grid.Grid, opponentHand = 0):
        print("Recycling and playing")
        
    def storeTrace(self, node):
        #Store number of leaves i.e. number of times e(n) is used
        self.traceBuffer.append(str(node.countLeaves()))
        #Store score of final decision
        self.traceBuffer.append(str(node.score))
        #Blank space
        self.traceBuffer.append("")
        
        #Score of all level 2 nodes
        for option in node.branches:
            self.traceBuffer.append(str(option.score))
        #Blank space
        self.traceBuffer.append("")
        
    def choseDotsOrColors(self):
        temp = random.randint(0,9)%2
        
        if(temp == 0):
            print("AI has chosen colors")
        else:
            print("AI has chosen dots")
        
        return temp