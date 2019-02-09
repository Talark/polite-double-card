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
    def turnStart(self, board : Grid.Grid):
        print("\nTurn has started")
        print("Here's the current board:\n")
        board.display()
        if(self.hand > 0):
            print("\nRegular play initiated")
            self.hand -= 1
            return self.playFromHand(board)
        else:
            print("\nRecycle play initiated")
            return self.recycleAndPlay(board)
            
    
    #Prompt user for regular play command and ensure it's of the correct format
    def playFromHand(self, board : Grid.Grid):
        print("Playing from hand")
        command = input("Where would you like to play?")
        return command
        
    #Prompt user for recycle play command and ensure it's of the correct format
    def recycleAndPlay(self, board : Grid.Grid):
        print("Recycling and playing")
        command = input("Where would you like to play?")
        return command