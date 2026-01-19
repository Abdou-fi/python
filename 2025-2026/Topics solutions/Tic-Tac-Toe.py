# Tic-Tac-Toe: Implement the classic 3x3 game, starting with a text-based version and potentially adding a graphical interface (GUI) or an AI opponent later. 
# This is a simple text-based implementation.

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Print a separator line

def check_winner(board):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True 

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))

        if board[row-1][col-1] == " ":
            board[row-1][col-1] = current_player
        else:
            print("Cell already taken, try again.")
            continue
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
