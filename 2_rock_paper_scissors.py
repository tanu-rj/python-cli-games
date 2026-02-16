"""
Rock Paper Scissors Game
Play against the computer
"""

import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def play_rock_paper_scissors():
    print("=" * 50)
    print("WELCOME TO ROCK PAPER SCISSORS!")
    print("=" * 50)
    
    player_score = 0
    computer_score = 0
    
    while True:
        print(f"\nYour Score: {player_score} | Computer Score: {computer_score}")
        
        player_choice = input("Choose (rock/paper/scissors) or 'quit': ").lower().strip()
        
        if player_choice == "quit":
            break
        
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        
        if result == "win":
            print("✅ You win this round!")
            player_score += 1
        elif result == "lose":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")
    
    print(f"\n" + "=" * 50)
    print("FINAL RESULTS")
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    if player_score > computer_score:
        print("🏆 You're the overall winner!")
    elif computer_score > player_score:
        print("🤖 Computer is the overall winner!")
    else:
        print("🤝 It's a tie overall!")
    print("=" * 50)

if __name__ == "__main__":
    play_rock_paper_scissors()
