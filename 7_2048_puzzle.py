"""
2048 Puzzle Game (Simplified)
Combine numbered tiles to reach 2048
"""

import random

def create_board():
    board = [[0] * 4 for _ in range(4)]
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 2, 2, 4])

def print_board(board):
    print("\n" + "=" * 25)
    for row in board:
        print("|".join(f"{val:^5}" for val in row))
        print("-" * 25)
    print()

def move_left(board):
    for row in board:
        # Remove zeros
        non_zero = [val for val in row if val != 0]
        # Merge
        merged = []
        i = 0
        while i < len(non_zero):
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged.append(non_zero[i] * 2)
                i += 2
            else:
                merged.append(non_zero[i])
                i += 1
        # Pad with zeros
        while len(merged) < 4:
            merged.append(0)
        row[:] = merged
    return board

def rotate_board_cw(board):
    return [[board[3-j][i] for j in range(4)] for i in range(4)]

def rotate_board_ccw(board):
    return [[board[j][3-i] for j in range(4)] for i in range(4)]

def move(board, direction):
    original = [row[:] for row in board]
    
    if direction == "left":
        move_left(board)
    elif direction == "right":
        board[:] = rotate_board_cw(rotate_board_cw(rotate_board_cw(rotate_board_cw([row[:] for row in board]))))
        board[:] = rotate_board_cw(rotate_board_cw(rotate_board_cw(move_left(rotate_board_ccw(rotate_board_ccw(rotate_board_ccw(board)))))))
    elif direction == "up":
        board[:] = rotate_board_ccw(move_left(rotate_board_cw(board)))
    elif direction == "down":
        board[:] = rotate_board_cw(move_left(rotate_board_ccw(board)))
    
    if board != original:
        add_new_tile(board)
        return True
    return False

def check_game_over(board):
    # Check if any empty cells
    if any(0 in row for row in board):
        return False
    # Check if any moves possible
    for i in range(4):
        for j in range(4):
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
    return True

def play_2048():
    print("=" * 50)
    print("WELCOME TO 2048!")
    print("=" * 50)
    print("\nUse arrow keys or WASD to move:")
    print("w/up = up, s/down = down, a/left = left, d/right = right")
    print("q = quit\n")
    
    board = create_board()
    add_new_tile(board)
    add_new_tile(board)
    
    moves = 0
    max_tile = 0
    
    while True:
        print_board(board)
        max_tile = max(max(row) for row in board)
        print(f"Moves: {moves} | Max tile: {max_tile}")
        
        if any(2048 in row for row in board):
            print("🎉 You reached 2048! Congratulations!")
            break
        
        if check_game_over(board):
            print("💀 Game Over! No more moves possible.")
            break
        
        move_input = input("Move (w/a/s/d or q to quit): ").lower().strip()
        
        if move_input == "q":
            print("Thanks for playing!")
            break
        
        direction = None
        if move_input in ["w", "up"]:
            direction = "up"
        elif move_input in ["s", "down"]:
            direction = "down"
        elif move_input in ["a", "left"]:
            direction = "left"
        elif move_input in ["d", "right"]:
            direction = "right"
        
        if direction and move(board, direction):
            moves += 1
        elif direction:
            print("Can't move in that direction!")
    
    if input("\nPlay again? (yes/no): ").lower() == "yes":
        play_2048()

if __name__ == "__main__":
    play_2048()
