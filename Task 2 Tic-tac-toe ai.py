import random

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")

def check_win(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Checks if the board is completely filled."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def get_empty_cells(board):
    """Returns a list of coordinates for empty cells on the board."""
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))
    return empty_cells

def minimax(board, depth, is_maximizing):
    """Implementation of the Minimax algorithm for the AI."""
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = ' '
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Finds the best move for the AI using Minimax."""
    best_score = -float('inf')
    best_move = None

    for row, col in get_empty_cells(board):
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move

def main():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            while True:
                try:
                    row, col = map(int, input("Enter your move (row and column, 0-2): ").split())
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                        board[row][col] = 'X'
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter two numbers separated by a space.")
        else:
            print("AI's turn...")
            row, col = find_best_move(board)
            board[row][col] = 'O'

        if check_win(board, current_player):
            print_board(board)
            print(current_player + " wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
