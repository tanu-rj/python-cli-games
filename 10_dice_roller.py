"""
Dice roller Game - Console Version
Roll dice and win by getting certain numbers
"""

import random

def play_dice_game():
    print("=" * 50)
    print("WELCOME TO DICE ROLLER GAME!")
    print("=" * 50)
    
    while True:
        print("\nGame Modes:")
        print("1. Roll and Compare (vs Computer)")
        print("2. Pig Dice (Accumulate points)")
        print("3. Exit")
        
        choice = input("\nChoose a mode (1-3): ").strip()
        
        if choice == "1":
            play_roll_and_compare()
        elif choice == "2":
            play_pig_dice()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

def play_roll_and_compare():
    print("\n" + "=" * 50)
    print("ROLL AND COMPARE")
    print("=" * 50)
    
    player_score = 0
    computer_score = 0
    rounds = 0
    max_rounds = 5
    
    while rounds < max_rounds:
        rounds += 1
        print(f"\nRound {rounds}/{max_rounds}")
        
        input("Press Enter to roll the dice...")
        
        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        
        print(f"You rolled: {player_roll} 🎲")
        print(f"Computer rolled: {computer_roll} 🎲")
        
        if player_roll > computer_roll:
            print("✅ You win this round!")
            player_score += 1
        elif computer_roll > player_roll:
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")
        
        print(f"Score: You {player_score} - Computer {computer_score}")
    
    print("\n" + "=" * 50)
    print("GAME COMPLETE!")
    print(f"Final Score: You {player_score} - Computer {computer_score}")
    
    if player_score > computer_score:
        print("🏆 You're the winner!")
    elif computer_score > player_score:
        print("🤖 Computer is the winner!")
    else:
        print("🤝 It's a tie overall!")
    print("=" * 50)

def play_pig_dice():
    print("\n" + "=" * 50)
    print("PIG DICE")
    print("Roll to accumulate points. Roll 1 to lose all points this turn.")
    print("First to 100 points wins!")
    print("=" * 50)
    
    player_total = 0
    computer_total = 0
    
    while player_total < 100 and computer_total < 100:
        print(f"\nYour Score: {player_total} | Computer Score: {computer_total}")
        
        # Player turn
        player_turn_score = 0
        player_continues = True
        
        print("\n🎮 Your turn!")
        
        while player_continues:
            roll = random.randint(1, 6)
            print(f"You rolled: {roll}")
            
            if roll == 1:
                print("💀 You rolled a 1! You lose all points this turn!")
                player_turn_score = 0
                player_continues = False
            else:
                player_turn_score += roll
                print(f"Turn score: {player_turn_score}")
                
                choice = input("Roll again or hold? (r/h): ").lower().strip()
                if choice != "r":
                    player_total += player_turn_score
                    print(f"✅ You held! Total: {player_total}")
                    player_continues = False
        
        if player_total >= 100:
            break
        
        # Computer turn
        computer_turn_score = 0
        print("\n🤖 Computer's turn...")
        
        while True:
            roll = random.randint(1, 6)
            print(f"Computer rolled: {roll}")
            
            if roll == 1:
                print("💀 Computer rolled a 1! Computer loses points this turn!")
                computer_turn_score = 0
                break
            else:
                computer_turn_score += roll
                print(f"Computer turn score: {computer_turn_score}")
                
                # Simple AI: hold on 20+ or if close to winning
                if computer_turn_score >= 20 or (computer_total + computer_turn_score >= 90):
                    computer_total += computer_turn_score
                    print(f"✅ Computer holds! Total: {computer_total}")
                    break
    
    print("\n" + "=" * 50)
    print("GAME COMPLETE!")
    print(f"Final Score: You {player_total} - Computer {computer_total}")
    
    if player_total >= 100:
        print("🏆 You're the winner!")
    else:
        print("🤖 Computer is the winner!")
    print("=" * 50)

if __name__ == "__main__":
    play_dice_game()
