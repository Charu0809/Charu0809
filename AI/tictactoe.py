import math

# Define the Tic-Tac-Toe board as a list
board = [' ' for _ in range(9)]

# Function to display the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Check for a winner or if the board is full
def check_winner(b, player):
    win_conditions = [
        [b[0], b[1], b[2]],
        [b[3], b[4], b[5]],
        [b[6], b[7], b[8]],
        [b[0], b[3], b[6]],
        [b[1], b[4], b[7]],
        [b[2], b[5], b[8]],
        [b[0], b[4], b[8]],
        [b[2], b[4], b[6]],
    ]
    return [player] * 3 in win_conditions

def is_board_full(b):
    return ' ' not in b

# Minimax algorithm with Alpha-Beta Pruning
def minimax(b, depth, is_maximizing, alpha, beta):
    if check_winner(b, 'O'):
        return 1
    elif check_winner(b, 'X'):
        return -1
    elif is_board_full(b):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                eval = minimax(b, depth + 1, False, alpha, beta)
                b[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                eval = minimax(b, depth + 1, True, alpha, beta)
                b[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find the best move for the AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Play the game
def play_game():
    print("Tic-Tac-Toe Game! You are 'X' and the AI is 'O'")
    print_board()

    while True:
        # Human move
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[human_move] = 'X'

        print_board()
        
        if check_winner(board, 'X'):
            print("Congratulations! You won!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = 'O'
        print("AI plays move:", ai_move + 1)
        print_board()

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

# Run the game
play_game()