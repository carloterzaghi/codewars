#Description:

# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? 
# Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]

# We want our function to return:

# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).

# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

# Link for Kata: https://www.codewars.com/kata/525caa5c1bf619d28c000335

# My code:

def is_solved(board):
    if [board[0][0],board[1][1],board[2][2]] in [[1,1,1],[2,2,2]]: return board[0][0]
    if [board[0][2],board[1][1],board[2][0]] in [[1,1,1],[2,2,2]]: return board[0][2]
    for i in range(3):
        if [board[0][i], board[1][i], board[2][i]] in [[1,1,1],[2,2,2]]: return board[0][i]
    for line in board: 
        if line in [[1,1,1],[2,2,2]]: return line[0]
    if 0 in board[0] or 0 in board[1] or 0 in board[2]: return -1
    return 0