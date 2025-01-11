# Tic-Tac-Toe-Game
Our python code lets you play Tic-Tac-Toe in two ways:  
  1. One Player Mode: You against the computer with a smart opponent.
  2. Two Player Mode: Play against a friend.
The computer's moves in the one-player mode are determined using the minimax algorithm,  making it a challenging opponent.
# **How to Play** 
1. Choose the game mode: 
  • One Player (1). 
  • Two Players (2). 
2. If you're playing against the computer, it randomly decides who goes first. 
3. Each turn, a player picks a spot on the board to place their 'X' or 'O'. 
4. The game ends when someone wins or the board is full, resulting in a draw. 
5. After the game ends you can choose to play again or exit. 
# Functions
1. printStart(): 
  • Shows you where each number corresponds on the Tic-Tac-Toe board. 
2. printBoard(board): 
  • Displays the current state of the Tic-Tac-Toe board. 
3. spaceIsFree(position): 
  • Checks if a spot on the board is empty. 
4. insertLeter(leter, position): 
  • Places your 'X' or 'O' on the board and checks if you've won or it's a draw. 
5. checkForWin(): 
  • Figures out if someone has won. 
6. checkWhichMarkWon(mark): 
  • Checks which player won based on the winning combinations. 
  • We used any() and all() functions to check the winning combinations. 
7. checkDraw(): 
  • Checks if the game ended in a draw. 
8. playerMove(player): 
  • Takes your input to make a move. 
9. compMove(): 
  • Makes the computer's move using an AI algorithm. 
10. minimax(board, depth, isMaximizing): 
  • Smartly evaluates the best move for the computer. 
11. Game Loop: 
  • Manages the game flow, taking turns and checking for a winner. 
# **Important Points** 
  • In our code we used os and random libraries for clearing the screen and generating random 
    numbers. 
  • It handles mistakes during player moves. 
  • After each game, you can choose to play again or exit.
