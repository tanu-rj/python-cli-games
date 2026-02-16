"""
Guess the Number Game
Try to guess the random number between 1 and 100
"""

import random

def play_guess_game():
    print("=" * 50)
    print("WELCOME TO GUESS THE NUMBER GAME!")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100...")
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nGuess #{attempts + 1} (You have {max_attempts - attempts} attempts left): "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
                
            attempts += 1
            
            if guess == number:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
            elif guess < number:
                print("📍 Too low! Try higher.")
            else:
                print("📍 Too high! Try lower.")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    else:
        print(f"\n💔 Game Over! The number was {number}")
    
    if input("\nPlay again? (yes/no): ").lower() == "yes":
        play_guess_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_guess_game()
