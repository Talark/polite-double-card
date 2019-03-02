# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:32:20 2019

@author: m_taran
"""

import Player as Player
import Grid as Grid

class AI(Player.Player):
    
    def __init__(self):
        super(AI,self).__init__()
    
    def turnStart(self, board : Grid.Grid):
        if(self.hand>0):
            self.playFromHand(board)
        else:
            self.recycleAndPlay(board)
    
    def playFromHand(self, board : Grid.Grid):
        print("Playing from hand")
        
    def recycleAndPlay(self, board : Grid.Grid):
        print("Recycling and playing")