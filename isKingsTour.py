# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.

def isLegalMove(board, row, col):
    n = len(board)
    k = board[row][col]
    if row+1 < n:
        if board[row+1][col] == k+1:
            return True
        if col+1 < n and board[row+1][col+1] == k+1:
            return True
        if col-1 >= 0 and board[row+1][col-1] == k+1:
            return True
    if row-1 < n:
        if board[row-1][col] == k+1:
            return True
        if col+1 < n and board[row-1][col+1] == k+1:
            return True
        if col-1 >= 0 and board[row-1][col-1] == k+1:
            return True
    if col+1 < n and board[row][col+1] == k+1:
        return True
    if col-1 >= 0 and board[row][col-1] == k+1:
        return True
    return False
 
def isKingsTour(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and board[i][j] < n**2 and not isLegalMove(board, i, j):
                return False
    return True

board = [ 
    [ 3, 2, 1 ], 
    [ 6, 4, 9 ],
    [ 5, 7, 8 ]
 ]

assert(isKingsTour(board) == True)

board = [ 
    [ 1, 2, 3 ], 
    [ 7, 4, 8 ],
    [ 6, 5, 9 ]
 ]

assert(isKingsTour(board) == False)

board = [ 
    [ 3, 2, 1 ], 
    [ 6, 4, 0 ],
    [ 5, 7, 8 ]
 ]

assert(isKingsTour(board) == False)

print("All test cases passed.")