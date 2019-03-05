# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:32:20 2019

@author: m_taran
"""

import Player as Player
import Grid as Grid
import Node as Node

class AI(Player.Player):
    
    def __init__(self):
        super(AI,self).__init__()
        self.depth = 1
        
    def setDepth(self, value : int):
        self.depth = value
    
    def turnStart(self, board : Grid.Grid, opponentHand = 0):
        if(self.hand>0):
            return self.playFromHand(board, opponentHand)
        else:
            return self.recycleAndPlay(board, opponentHand)
    
    def playFromHand(self, board : Grid.Grid, opponentHand = 0):
        print("Playing from hand")
        nody = Node.Node(self.hand,opponentHand,self.playType,1-self.playType,board, self.depth)

        nody.buildChildNodes()

        nody.makeMove()
        
        return nody.command
        
    def recycleAndPlay(self, board : Grid.Grid, opponentHand = 0):
        print("Recycling and playing")
        nody = Node.Node(self.hand,opponentHand,self.playType,1-self.playType,board, self.depth)

        nody.buildChildNodes()

        nody.makeMove()
        
        return nody.command