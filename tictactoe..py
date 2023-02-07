# Global Variables


board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# If game still going
game_still_going = True

# who won?

winner = None

# who turn is
current_player = "x"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "x" or winner == "o":
        print(winner + "won")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    
  print(player + " turn")
  position = input("Choose from 1-9: ")

  valid=False
  while not valid:
    
      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input(" please Choose from 1-9: ")

      position = int(position) - 1

      if board[position] == "_":
        valid=True
      else:    
        print(" Overwrite,try again")

  board[position] = player

  display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
        # there was a win
    elif column_winner:
        winner = column_winner
        # there was a win
    elif diagonal_winner:
        winner = diagonal_winner
        # there was a win
    # check rows, column, diagonals
    else:
        # there is no win
        winner = None
    return


def check_rows():
    # set up global variables
    global game_still_going
    # check have all the same values and is not empty
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner x or o
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    # check have all the same values and is not empty

    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[3] == board[5] == board[8] != "_"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():
    global game_still_going
    # check have all the same values and is not empty

    diagonals_1 = board[0] == board[4] == board[8] != "_"
    diagonals_2 = board[6] == board[4] == board[2] != "_"

    if diagonals_1 or diagonals_2:
        game_still_going = False
    # return the winner x or o
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]

    return


def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False

    return


def flip_player():
    # global variables
    global current_player
    # if the current player was x than change to o
    if current_player == "x":
        current_player = "o"
        # if the current player was x than change to o1

    elif current_player == "o":
        current_player = "x"
    return
#dd

play_game()
