heights = [1.4, 1.3, 1.5, 2, 1.4, 1.5, 1]
print(heights)
heights.sort()
print(heights)
heights.reverse()
print(heights)

x = "x"
o = "o"
empty = "_"

board = [[x, empty, o], [empty, x, o], [x, empty, empty]]
print(board)

emails = "zebra@zoo.com, red@colors.com, tom@book.com, carrot@veg.com"
emails_list = emails.split(",")
print(emails_list)

###########################
### Quickcheck Exercise ###
###########################
def check_player_win(board, token):
    """
    board: list of strings representing a tic-tac-toe board where a
           row is a string of 3 tokens
    token: string representing either x or o
    Checks 8 possible winning combinations for a tic-tac-toe win:
    3 rows matching the token, 3 columns matching the token, 
    or 2 diagonals matching the token.
    Returns True if the token got 3 in a row with any of the 
    possible combinations, and returns False otherwise.
    """
    row1 = (board[0][0] == board[0][1] == board[0][2] == token)
    row2 = (board[1][0] == board[1][1] == board[1][2] == token)
    row3 = (board[2][0] == board[2][1] == board[2][2] == token)
    col1 = (board[0][0] == board[1][0] == board[2][0] == token)
    col2 = (board[0][1] == board[1][1] == board[2][1] == token)
    col3 = (board[0][2] == board[1][2] == board[2][2] == token)
    diag1 = (board[0][0] == board[1][1] == board[2][2] == token)
    diag2 = (board[2][0] == board[1][1] == board[0][2] == token)
    return row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2

game = "xox|oox|xxo"
board = game.split("|")

winner_o = check_player_win(board, "o")
winner_x = check_player_win(board, "x")

if not winner_o and not winner_x:
    print("It's a draw!")
elif winner_o:
    print("o is the winner!")    
elif winner_x:
    print("x is the winner!")  
    