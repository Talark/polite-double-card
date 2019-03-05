# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:47:52 2019

@author: m_taran
"""

import Grid as Grid
import Human as Human
import AI as AI

class GameController:
    
    def __init__(self):
        self.gameBoard = Grid.Grid()
        #Depending on how you want turn to be used it can also be set to 60
        self.turn = 1
    
    #This method runs through a game for human vs human
    def runHumanVSHuman(self):
        self.player1 = Human.Human()
        self.player2 = Human.Human()
        #Prompt player1 for dots or colors
        playType = None
        while(playType!="0" and playType!="1"):
            playType = input("Dots or Colors?? ENTER 0 for colors, 1 for dots: ")
        self.player1.setPlayType(int(playType))
        self.player2.setPlayType(1 - int(playType))
        #run through game logic (turns, ending games, move legality, communication between grid and players)
        #Turns
        
        while self.turn <= 60:
            if self.turn % 2 == 1:
                command = self.player1.turnStart(self.gameBoard)
                if self.gameBoard.playCard(command):
                    self.gameBoard.currentPlayer = self.player2.playType
                    self.turn += 1
                    self.player1.hand -= 1
                    print("Checking for wins originating from command location and it's neighbor")
                    if self.gameBoard.checkForWin(command) == True:
                        self.gameBoard.printMsgBuffer()
                        break
                    
            else:
                command = self.player2.turnStart(self.gameBoard)
                if self.gameBoard.playCard(command):
                    self.gameBoard.currentPlayer = self.player1.playType
                    self.turn += 1
                    self.player2.hand -= 1
                    print("Checking for wins originating from command location and it's neighbor")
                    if self.gameBoard.checkForWin(command) == True:
                        self.gameBoard.printMsgBuffer()
                        break
                    
            self.gameBoard.printMsgBuffer()
            
        self.gameBoard.display()
    #This method will modify logic from above for a human vs ai game
    def runHumanVSAI(self):
        
        aiFirst = None
        while(aiFirst!="0" and aiFirst!="1"):
            aiFirst = input("Is the AI playing first? ENTER 0 for yes, 1 for no: ")
        
        if(aiFirst == "0"):
            self.player1 = AI.AI()
            self.player1.setDepth(2)
            self.player2 = Human.Human()
        else:
            self.player2 = AI.AI()
            self.player2.setDepth(2)
            self.player1 = Human.Human()
        
        #Prompt player1 for dots or colors
        playType = None
        while(playType!="0" and playType!="1"):
            playType = input("Is player1 playing Dots or Colors?? ENTER 0 for colors, 1 for dots: ")
        self.player1.setPlayType(int(playType))
        self.player2.setPlayType(1 - int(playType))
        
        
        while self.turn <= 60:
            if self.turn % 2 == 1:
                command = self.player1.turnStart(self.gameBoard)
                if self.gameBoard.playCard(command):
                    self.gameBoard.currentPlayer = self.player2.playType
                    self.turn += 1
                    self.player1.hand -= 1
                    print("Checking for wins originating from command location and it's neighbor")
                    if self.gameBoard.checkForWin(command) == True:
                        self.gameBoard.printMsgBuffer()
                        break
                elif(aiFirst=="0"):
                    print("AI made an illegal move! Player2 wins!")
                    self.gameBoard.printMsgBuffer()
                    break
            else:
                command = self.player2.turnStart(self.gameBoard)
                if self.gameBoard.playCard(command):
                    self.gameBoard.currentPlayer = self.player1.playType
                    self.turn += 1
                    self.player2.hand -= 1
                    print("Checking for wins originating from command location and it's neighbor")
                    if self.gameBoard.checkForWin(command) == True:
                        self.gameBoard.printMsgBuffer()
                        break
                elif(aiFirst=="1"):
                    print("AI made an illegal move! Player1 wins!")
                    self.gameBoard.printMsgBuffer()
                    break
                    
            self.gameBoard.printMsgBuffer()
            
        self.gameBoard.display()