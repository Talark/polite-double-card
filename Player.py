# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:48:45 2019

@author: m_taran
"""
import Grid as Grid

class Player:
    
    def __init__(self):
        self.hand = 12
        self.playType = 0
    
    #0 should denote the player is using colors, 1 should denote the player is using dots
    def setPlayType(self, num):
        self.playType = num
    
    #The following methods are templates that should be copied into child classes and overridden
    def turnStart(self, board : Grid.Grid):
        print("Turn has started (Parent method called, this should not happen)")
    
    def playFromHand(self, board : Grid.Grid):
        print("Playing from hand (Parent method called, this should not happen)")
        
    def recycleAndPlay(self, board : Grid.Grid):
        print("Recycling and playing (Parent method called, this should not happen)")
    
    def getHandSize(self):
        return self.hand
    
    def getPlayType(self):
        return self.playType
    