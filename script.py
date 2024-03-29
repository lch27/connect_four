from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print("X Turn\nX selected", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), my_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


def random_eval(board):
    return random.randint(-100, 100)

def my_evaluate_board(board):
    if has_won(board, "X"):
        return float("Inf")
    if has_won(board, "O"):
        return -float("Inf")

    x_two_streak = 0
    o_two_streak = 0

    # Check horizontal streaks
    for column in range(len(board) - 1):
        for row in range(len(board[0])):
            if board[column][row] == "X" and board[column + 1][row] == "X":
                x_two_streak += 1
            if board[column][row] == "O" and board[column + 1][row] == "O":
                o_two_streak += 1

    # Check vertical streaks
    for column in range(len(board)):
        for row in range(len(board[0]) - 1):
            if board[column][row] == "X" and board[column][row + 1] == "X":
                x_two_streak += 1
            if board[column][row] == "O" and board[column][row + 1] == "O":
                o_two_streak += 1

    # Check diagonal streaks (from top-left to bottom-right)
    for column in range(len(board) - 1):
        for row in range(len(board[0]) - 1):
            if board[column][row] == "X" and board[column + 1][row + 1] == "X":
                x_two_streak += 1
            if board[column][row] == "O" and board[column + 1][row + 1] == "O":
                o_two_streak += 1

    for column in range(1, len(board)):
        for row in range(len(board[0]) - 1):
            if board[column][row] == "X" and board[column - 1][row + 1] == "X":
                x_two_streak += 1
            if board[column][row] == "O" and board[column - 1][row + 1] == "O":
                o_two_streak += 1

 return x_two_streak - o_two_streak

def new_board():
  board = make_board()
  select_space(board, 6, "X")
  select_space(board, 5, "X")
  select_space(board, 4, "O")
  select_space(board, 3, "O")
  return board

board = new_board()
print(my_evaluate_board(board))



two_ai_game()