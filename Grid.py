# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:45:55 2019

@author: m_taran
"""
#Feel free to add methods as needed

import DoubleCard.HalfCard as HalfCard

class Grid:
    
    def __init__(self):
        #lastMove contains the command from the last move
        self.lastMove = "None"
        #currentPlayer should switch from 1 to 0 and back, this lets it be used as a conditional
        self.currentPlayer = 1
        #board is a dictionary of dictionaries where A1 is the bottom left of the board
        #letters denote columns and numbers denote rows
        self.board = {
                "A": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "B": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "C": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "D": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "E": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "F": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "G": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            },
                "H": {
                        "1": HalfCard.HalfCard(0,0,""),
                        "2": HalfCard.HalfCard(0,0,""),
                        "3": HalfCard.HalfCard(0,0,""),
                        "4": HalfCard.HalfCard(0,0,""),
                        "5": HalfCard.HalfCard(0,0,""),
                        "6": HalfCard.HalfCard(0,0,""),
                        "7": HalfCard.HalfCard(0,0,""),
                        "8": HalfCard.HalfCard(0,0,""),
                        "9": HalfCard.HalfCard(0,0,""),
                        "10": HalfCard.HalfCard(0,0,""),
                        "11": HalfCard.HalfCard(0,0,""),
                        "12": HalfCard.HalfCard(0,0,"")
                            }
                }
    
    #We need to change the input string to a list
    def inputToList(self, inputString): 
        inputString = "A B C D"
        command = inputString.split()
        return command
    
    #should only set appropriate cells of grid is move is legal
    #must return false if not legal, true otherwise
    def playCard(self, command):
        commandFormated = self.inputToList(command)
        print("Putting",command,"in grid if legal")
        isLegal = self.moveIsLegal(commandFormated)
        
        
    
    #same as above, but has an additional legality check (ensure command targets 2 halves of 1 piece and piece is not under others)
    #can modify recycle command into a play command afterwards (just an implementation option if you want to do it that way)
    def recycleAndPlayCard(self, command):
        print("Modifying grid and command for recycle if legal")
    
    #Determine if move is legal and returns true or false
    def moveIsLegal(self, command):
        print("Checking if move is legal")
        
    #This method should receive coordinates from which it needs to radiate out from to check for a win
    #In general this method must check for wins from 2 origin points since cards have 2 halves that can be part of a 4-set
    def checkForWin(self, command):
        print("Checking for wins originating from command location")
    
    #Figure this might be usefull later on for AI implementation since dictionary accessing with indeces can get messy code wise
    def toList(self):
        print("Here's the grid as a list")
    
    #Self explanatory
    def display(self):
        print("*throws board in face*")