import os
import random
 
def printStart():
    print("Positions are as follow:")
    print(' 1 | 2 | 3 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')    
    print('---+---+---')
    print(' 7 | 8 | 9 ')
    print("\n")
   
def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print("\n")
 
 
def spaceIsFree(position):
    return ( board[position] == ' ')
 
 
def insertLetter(letter, position):
    try:
        if (position > 0 and position < 10) and spaceIsFree(position):
            board[position] = letter
            printBoard(board)
            if (checkForWin()):
                os.system('cls')
                printBoard(board)
                if letter == 'X':
                    if mode == 1:    
                        print("Bot wins!")
                    else:
                        print("Player 1 wins!")
                    return True
                else:
                    if mode == 1:
                        print("Player wins!")
                    else:
                        print("Player 2 wins!")
                    return True
            if (checkDraw()):
                os.system('cls')
                printBoard(board)
                print("Draw!")
                return True
        else:
            print("Can't insert there!")
            position = int(input("Please enter new position:  "))
            insertLetter(letter, position)
    except ValueError:
        position = int(input("Invalid input. Please enter a valid number:"))
        insertLetter(letter, position)
 
 
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
 
def checkWhichMarkWon(mark):
    winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                            [1, 4, 7], [2, 5, 8], [3, 6, 9],  
                            [1, 5, 9], [7, 5, 3]]
    return any(all(board[pos] == mark for pos in comb) for comb in winning_combinations)
 
 
 
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True
 
 
def playerMove(player):
    if player == 'O':
        position = int(input("Enter the position for 'O':  "))
    else:
        position = int(input("Enter the position for 'X':  "))
    flag = insertLetter(player, position)
    return flag
 
 
def compMove():
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    flag = insertLetter(bot, bestMove)
    return flag
 
 
def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0
    if (isMaximizing):
        bestScore = -100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
 
    else:
        bestScore = 100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore
 
player = 'O'
bot = 'X'
 
EndGame = False
while not EndGame:
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
   
    er = True
    flag = False
    er2 = False
    while er:
        print ('   |------------| ')
        print ('   |  X O Game  | ')
        print ('   |------------|\n')
        print ('1. one player.')
        print ('2. two player.')
        try:
            mode = int(input('choose mode of play: '))
            os.system('cls')
            if mode == 1:
                random_number = random.randint(1, 2)
                if random_number == 1:
                    print("Computer goes first! Good luck.")
                    while not flag:
                        printStart()
                        flag = compMove()
                        if flag:
                            break
                        flag = playerMove(player)
                        if flag:
                            break
                        os.system('cls' )
                    er = False
                else:
                    print("You go first! good luck.")
                    while not flag:
                        printStart()
                        printBoard(board)
                        flag = playerMove(player)
                        if flag:
                            break
                        os.system('cls')
                        flag = compMove()
                        if checkForWin():
                            break
                        else:
                            os.system('cls')
                    er = False
            elif mode == 2:
                while not flag:
                    printStart()
                    printBoard(board)
                    flag = playerMove('X')
                    if flag:
                        break
                    os.system('cls' )
                    printStart()
                    printBoard(board)
                    flag = playerMove('O')
                    if flag:
                        break
                    os.system('cls')
                er = False
            else:
                os.system('cls' )
        except ValueError:
            os.system('cls')
    while not er2:
        try:
            print ("\n--------------------------")
            print ("Choose the option you want")
            print ("--------------------------")
            print ("1. Replay the game.\n2. exit game.")
            x =int(input ("Enter your choice: "))
            if x == 1 :
                er2 = True
            elif x == 2 :
                er2 = True
                EndGame = True
            else:
                os.system('cls' )
        except ValueError:
                os.system('cls')
        os.system('cls')