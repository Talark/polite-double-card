# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:47:52 2019

@author: m_taran
"""

import DoubleCard.Grid as Grid
import DoubleCard.Human as Human

class GameController:
    
    def __init__(self):
        self.gameBoard = Grid.Grid()
        #Depending on how you want turn to be used it can also be set to 60
        self.turn = 0
    
    #This method runs through a game for human vs human
    def runHumanVSHuman(self):
        self.player1 = Human.Human()
        self.player2 = Human.Human()
        #Prompt player1 for dots or colors
        #run through game logic (turns, ending games, move legality, communication between grid and players)
    
    #This method will modify logic from above for a human vs ai game
    def runHumanVSAI(self):
        print("Not yet implemented")