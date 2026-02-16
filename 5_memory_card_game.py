"""
Memory Card Game
Match pairs of cards
"""

import random
import time

def play_memory_game():
    print("=" * 50)
    print("WELCOME TO MEMORY CARD GAME!")
    print("=" * 50)
    
    # Game difficulty selection
    while True:
        difficulty = input("\nSelect difficulty:\n1. Easy (4x4 = 8 pairs)\n2. Medium (4x6 = 12 pairs)\n3. Hard (6x6 = 18 pairs)\nChoice (1-3): ").strip()
        if difficulty in ['1', '2', '3']:
            break
        print("Invalid choice!")
    
    if difficulty == '1':
        grid_size = 4
        num_pairs = 8
    elif difficulty == '2':
        grid_size = 4
        num_pairs = 12
    else:
        grid_size = 6
        num_pairs = 18
    
    # Create cards
    cards = list(range(1, num_pairs + 1)) * 2
    random.shuffle(cards)
    
    revealed = [[False] * grid_size for _ in range(4 if grid_size == 4 else 6)]
    matched = [[False] * grid_size for _ in range(4 if grid_size == 4 else 6)]
    
    matches = 0
    moves = 0
    start_time = time.time()
    
    def show_grid():
        print("\n")
        for i in range(len(revealed)):
            for j in range(len(revealed[i])):
                if matched[i][j]:
                    print(" ✅ ", end=" ")
                elif revealed[i][j]:
                    print(f" {cards[i * grid_size + j]:2d} ", end=" ")
                else:
                    print(f" [{i * grid_size + j + 1:2d}] ", end=" ")
            print()
        print()
    
    print("\nCards are hidden. Choose by number (1-{})\n".format(grid_size * (6 if grid_size == 6 else 4)))
    
    while matches < num_pairs:
        show_grid()
        print(f"Matches: {matches}/{num_pairs} | Moves: {moves}")
        
        try:
            first_pos = int(input("Choose first card: ")) - 1
            first_row = first_pos // grid_size
            first_col = first_pos % grid_size
            
            if first_pos < 0 or first_pos >= len(cards) or matched[first_row][first_col]:
                print("Invalid card!")
                continue
            
            revealed[first_row][first_col] = True
            show_grid()
            
            second_pos = int(input("Choose second card: ")) - 1
            second_row = second_pos // grid_size
            second_col = second_pos % grid_size
            
            if second_pos < 0 or second_pos >= len(cards) or matched[second_row][second_col] or first_pos == second_pos:
                print("Invalid card!")
                revealed[first_row][first_col] = False
                continue
            
            revealed[second_row][second_col] = True
            show_grid()
            
            moves += 1
            
            if cards[first_pos] == cards[second_pos]:
                print("✅ Match found!")
                matched[first_row][first_col] = True
                matched[second_row][second_col] = True
                matches += 1
            else:
                print(f"❌ No match. Cards were {cards[first_pos]} and {cards[second_pos]}")
                time.sleep(1)
                revealed[first_row][first_col] = False
                revealed[second_row][second_col] = False
                
        except (ValueError, IndexError):
            print("Invalid input!")
            continue
    
    elapsed_time = time.time() - start_time
    print(f"\n🎉 Congratulations! You won in {moves} moves and {elapsed_time:.1f} seconds!")
    
    if input("Play again? (yes/no): ").lower() == "yes":
        play_memory_game()

if __name__ == "__main__":
    play_memory_game()
