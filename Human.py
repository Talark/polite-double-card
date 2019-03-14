# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:48:59 2019

@author: m_taran
"""

import Player as Player
import Grid as Grid

class Human(Player.Player):
    
    def __init__(self):
        super(Human,self).__init__()
    
    #Should detemine if player should perform regular or recycling move
    #Grid should not be modified here, it's only a parameter in the function to allow the AI to see the board once it's implemented
    def turnStart(self, board : Grid.Grid, opponentHand = 0):
        print("\nTurn has started")
        print("Here's the current board:\n")
        board.display()
        
        temp = ""
        
        while not self.checkFormat(temp,self.hand):
            
            if(not temp==""):
                print(temp,"has invalid format. Try again.")
            
            if(self.hand > 0):
                print("\nRegular play initiated")
                temp = self.playFromHand(board)
            else:
                print("\nRecycle play initiated")
                temp = self.recycleAndPlay(board)
        
        print(temp,"was accepted.")
        
        return temp.upper()
    
    #Prompt user for regular play command and ensure it's of the correct format
    def playFromHand(self, board : Grid.Grid, opponentHand = 0):
        print("Playing from hand")
        command = input("Where would you like to play?")
        return command
        
    #Prompt user for recycle play command and ensure it's of the correct format
    def recycleAndPlay(self, board : Grid.Grid, opponentHand = 0):
        print("Recycling and playing")
        command = input("Where would you like to play?")
        return command
    
    #Check format of command
    def checkFormat(self, command, expected):
        charList = command.split()

        #check for empty string
        if len(charList)==0:
            return False

        #Check regular play format
        if(charList[0]=="0"):
            #Ensure it contains 4 elements
            if(expected == 0 or len(charList) != 4):
                return False
            
            #Check structure
            return (not charList[1].isalpha() and charList[2].isalpha() and not charList[3].isalpha())

        #Check recycle play format
        else:
            #Ensure it contains 7 elements
            if(expected != 0 or len(charList) != 7):
                return False
            
            #check first 4 elements
            one = (charList[0] and not charList[1].isalpha() and charList[2].isalpha() and not charList[3].isalpha())
            #check last 3 elements
            two = (not charList[4].isalpha() and charList[5].isalpha() and not charList[6].isalpha())
            
            return (one and two)