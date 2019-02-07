# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:48:59 2019

@author: m_taran
"""

import DoubleCard.Player as Player
import DoubleCard.Grid as Grid

class Human(Player.Player):
    
    def __init__(self):
        super()
    
    #Should detemine if player should perform regular or recycling move
    #Grid should not be modified here, it's only a parameter in the function to allow the AI to see the board once it's implemented
    def turnStart(self, board : Grid.Grid):
        print("Turn has started")
    
    #Prompt user for regular play command and ensure it's of the correct format
    def playFromHand(self, board : Grid.Grid):
        print("Playing from hand")
        
    #Prompt user for recycle play command and ensure it's of the correct format
    def recycleAndPlay(self, board : Grid.Grid):
        print("Recycling and playing")