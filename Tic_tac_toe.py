import math

board = [" " for _ in range(9)]

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return " " not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):  
        return 1
    elif is_winner(board, "X"):  
        return -1
    elif is_board_full(board):  
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board):
   
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move(board):
   
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Cell already taken.")
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1 and 9.")

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
      #player turn
        player_move(board)
        print_board(board)
        if is_winner(board, "X"):
            print("Congratulations, you win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break
        #Ai's turn 
        print("AI is making a move...")
        move = best_move(board)
        board[move] = "O"
        print_board(board)
        if is_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

tic_tac_toe()
