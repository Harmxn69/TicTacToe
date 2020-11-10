# ----- Global Variables -----

# board                         line 15
# display board                 line 29
# play game                     line 35
# handle turn                   line 59
# check win                     line 88
  # check rows                  line 112
  # check columns               line 132
  # check diagonals             line 152
# check tie                     line 169
# flip player                   line 176


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game still going
game_still_going = True

# Who won? or Tie?
winner = None

# Whose turn is it?
current_player = "X"

# Prints board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play a gme of TicTacToe
def play_game():

    # Display initial board
    display_board()

    # While the game is still going do this
    while game_still_going:

        # Handle a single turn of an arbritary player
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " is the winner.")
    elif winner == None:
        print("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You cant go there. Go again.")

  board[position] = player

  display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()



def check_for_winner():

    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # checks columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_rows():
    # Set up global variables
    global game_still_going
    # Check if any of the rows have all the same value and are not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Set up global variables
    global game_still_going
    # Check if any of the columns have all the same value and are not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variables
    global game_still_going
    # Check if any of the diagonals have all the same value and are not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # Global variables
    global current_player
    # If current player was X then change to O
    if current_player == "X":
        current_player = "O"
    # If current player is O then change to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()
