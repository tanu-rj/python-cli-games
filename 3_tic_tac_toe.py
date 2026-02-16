"""
Tic Tac Toe Game
Two-player game on a 3x3 grid
"""

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def print_positions():
    print("Position numbers:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    print("=" * 50)
    print("WELCOME TO TIC TAC TOE!")
    print("=" * 50)
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    
    print_positions()
    
    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                position = int(input(f"Player {current_player}, choose a position (1-9): "))
                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9!")
                    continue
                
                row = (position - 1) // 3
                col = (position - 1) % 3
                
                if board[row][col] != " ":
                    print("That position is already taken!")
                    continue
                
                board[row][col] = current_player
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        if check_winner(board, current_player):
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
        play_tic_tac_toe()

if __name__ == "__main__":
    play_tic_tac_toe()
