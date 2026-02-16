"""
Connect Four Game
Strategy game where players try to get 4 in a row
"""

def print_board(board):
    print("\n")
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("|---|---|---|---|---|---|---|")
    print("  1   2   3   4   5   6   7\n")

def check_winner(board, player):
    rows = len(board)
    cols = len(board[0])
    
    # Check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    
    # Check vertical
    for row in range(rows - 3):
        for col in range(cols):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    
    # Check diagonal (bottom-left to top-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    
    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_next_available_row(board, col):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == " ":
            return row
    return -1

def play_connect_four():
    print("=" * 50)
    print("WELCOME TO CONNECT FOUR!")
    print("=" * 50)
    
    rows, cols = 6, 7
    board = [[" " for _ in range(cols)] for _ in range(rows)]
    current_player = "X"
    game_over = False
    
    print("\nPlayer X = 🔴")
    print("Player O = 🟡\n")
    
    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                column = int(input("Choose a column (1-7): ")) - 1
                
                if column < 0 or column >= cols:
                    print("Please enter a number between 1 and 7!")
                    continue
                
                row = get_next_available_row(board, column)
                
                if row == -1:
                    print("That column is full!")
                    continue
                
                board[row][column] = "🔴" if current_player == "X" else "🟡"
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        if check_winner(board, "🔴" if current_player == "X" else "🟡"):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("🤝 It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
    
    if input("\nPlay again? (yes/no): ").lower() == "yes":
        play_connect_four()

if __name__ == "__main__":
    play_connect_four()
