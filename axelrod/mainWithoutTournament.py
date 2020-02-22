# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:14:30 2019

@author: Tanguy
"""

import axelrod as axl
import copy

theStrategies = [axl.Defector(), axl.TitForTat()]

def createBoard(dimension):
    board = []

    for i in range(dimension):
        line = []
        for j in range(dimension):

            # If we have the middle of the board we need to set a,n invader
#            if (i == j) and (i <= dimension/2 <= i + 1) and (j <= dimension/2 <= j + 1):
            if ((i == 2) and (j == 2)) or ((i == 6) and (j == 6)) :
                line.append(theStrategies[0])
            else:
                line.append(theStrategies[1])

        board.append(line)

    return board

def strategyNameToObject(name) :
    if name == "Defector" : 
        return axl.Defector()
    else : 
        return theStrategies[1]
        
def browseBoardAndActualize(board) :
    
    newBoard = copy.deepcopy(board)
    
    for i in range(len(board)) :
        
        for j in range(len(board[i])) :
            
            if (i == len(board)-1) and (j == len(board[i])-1) :
                
                pass
            
            elif i == len(board)-1 :
                
                match = axl.Match([board[i][j],board[i][j+1]], 1)
                match.play()
                
                if match.winner() == False :
                    
                    pass
                
                else :
                    
                    newBoard[i][j] = match.winner()
                    newBoard[i][j+1] = match.winner()
            
            elif j == len(board[i])-1 :
                
                match = axl.Match([board[i][j],board[i+1][j]], 1)
                match.play()
                
                if match.winner() == False :
                    
                    pass
                
                else :
                    
                    newBoard[i][j] = match.winner()
                    newBoard[i+1][j] = match.winner()
            else :
                
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] : 
                    pass
                else :
                    
                    firstMatch = axl.Match([board[i][j],board[i][j+1]])
                    secondMatch = axl.Match([board[i][j],board[i+1][j]])
                    firstMatch.play()
                    secondMatch.play()
                    
                    if firstMatch.winner() == False and secondMatch.winner() == False  :
                        pass
                            
                    else :
                        if firstMatch.winner() == board[i][j] :
                            newBoard[i][j+1]=firstMatch.winner()
                        if secondMatch.winner() == board[i][j] :
                            newBoard[i+1][j]=secondMatch.winner()
                        if firstMatch.winner() == board[i][j+1] :
                            newBoard[i][j]=firstMatch.winner()
                        if secondMatch.winner() == board[i+1][j] :
                            newBoard[i][j] = secondMatch.winner()
                        
    
    return newBoard

    
def printBoard(board):
    for b in board:
        formatedString = ""
        for b2 in b:
            if (str(b2) == str(theStrategies[0])):
                formatedString += ('# ')
            else:
                formatedString += ('- ')
        print(formatedString)
    print("")

board = createBoard(9)
printBoard(board)

for i in range(0,10) :
    board = browseBoardAndActualize(board)
    printBoard(board)
