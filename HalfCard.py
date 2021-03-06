# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:44:34 2019

@author: m_taran
"""

class HalfCard:
    
    #2 options for color and dot codes
    #1) nothing = 0, white = 1, emptyDot = 2, red = 3, filledDot = 4
    #2) nothing = 0, white = 1, emptyDot = 1, red = 2, filledDot = 2
    def __init__(self, c, d, n):
        self.color = c
        self.dot = d
        self.neighbor = n
    
    def setValues(self, col, d, neigh):
        self.color = col
        self.dot = d
        self.neighbor = neigh
    
    def display(self):
        print(self.color," ",self.dot," ",self.neighbor)
        
    def copyCard(self,card):
        self.color = card.color
        self.dot = card.dot
        self.neighbor = card.neighbor

    def __str__(self):
        if(self.color == 1 and self.dot == 1):
            return("WE")
        elif(self.color == 1 and self.dot == 2):
            return("WF")
        elif(self.color == 2 and self.dot == 1):
            return("RE")
        elif(self.color == 2 and self.dot == 2):
            return("RF")
        else:
            return("--")
