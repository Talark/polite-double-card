# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:47:52 2019

@author: m_taran
"""

import Grid as Grid
import Human as Human

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
        playType = None
        playType = input("Dots or Colors?? ENTER 0 for dots, 1 for colors: ")
        self.player1.setPlayType(playType)
        self.player2.setPlayType(1 - playType)
        #run through game logic (turns, ending games, move legality, communication between grid and players)
        #Turns
        oneChance = False
        
        while self.turn <= 60:
            if self.turn % 2 == 0:
                command = self.player1.turnStart(self.gameBoard)
                if self.gameBoard.playCard(command):
                    self.turn += 1
                    oneChance == False
                    if self.gameBoard.checkForWin(command) == True:
                        break
                # if one chance is not used, use it    
                else:
                    if oneChance == False:
                        oneChance = True
                    else:
                        print("Player 2 wins!!")
                        break
            else:
                command = self.player2.turnStart(self.gameBoard)
                if self.gameBoard.playCard(command):
                    self.turn += 1
                    oneChance == False
                    if self.gameBoard.checkForWin(command) == True:
                        break
                else:
                    if oneChance == False:
                        oneChance = True
                    else:
                        print("Player 1 wins!!")
                        break
            
            
    #This method will modify logic from above for a human vs ai game
    def runHumanVSAI(self):
        print("Not yet implemented")