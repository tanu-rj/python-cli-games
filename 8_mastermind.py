"""
Mastermind / Codebreaker Game
Guess the secret code with hints
"""

import random

COLORS = ['R', 'G', 'B', 'Y', 'P', 'O']  # Red, Green, Blue, Yellow, Purple, Orange
CODE_LENGTH = 4

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def get_feedback(secret, guess):
    """
    Returns (exact_matches, color_matches)
    exact_matches: correct color in correct position
    color_matches: correct color in wrong position
    """
    exact = sum(1 for i in range(CODE_LENGTH) if secret[i] == guess[i])
    
    secret_counts = {}
    guess_counts = {}
    
    for i in range(CODE_LENGTH):
        if secret[i] != guess[i]:
            secret_counts[secret[i]] = secret_counts.get(secret[i], 0) + 1
            guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1
    
    color_wrong_pos = 0
    for color in guess_counts:
        if color in secret_counts:
            color_wrong_pos += min(guess_counts[color], secret_counts[color])
    
    return exact, color_wrong_pos

def is_valid_guess(guess):
    if len(guess) != CODE_LENGTH:
        return False
    return all(color in COLORS for color in guess)

def play_mastermind():
    print("=" * 50)
    print("WELCOME TO MASTERMIND!")
    print("=" * 50)
    
    print(f"\nAvailable colors: {', '.join(COLORS)}")
    print(f"Guess a {CODE_LENGTH}-color code!")
    print("You have 12 attempts.\n")
    
    secret_code = generate_code()
    attempts = 0
    max_attempts = 12
    
    while attempts < max_attempts:
        print(f"Attempt {attempts + 1}/{max_attempts}")
        
        guess_str = input(f"Enter your guess ({CODE_LENGTH} colors, e.g., RBGY): ").upper().strip()
        guess = list(guess_str)
        
        if not is_valid_guess(guess):
            print(f"Invalid guess! Enter exactly {CODE_LENGTH} colors from: {', '.join(COLORS)}\n")
            continue
        
        attempts += 1
        
        if guess == secret_code:
            print(f"\n🎉 Congratulations! You guessed the code in {attempts} attempts!")
            print(f"The secret code was: {' '.join(secret_code)}")
            break
        
        exact, color_wrong = get_feedback(secret_code, guess)
        
        print(f"Your guess: {' '.join(guess)}")
        print(f"⚫ Exact matches (correct color, correct position): {exact}")
        print(f"⚪ Color matches (correct color, wrong position): {color_wrong}\n")
    
    else:
        print(f"\n💀 Game Over! The secret code was: {' '.join(secret_code)}")
    
    if input("Play again? (yes/no): ").lower() == "yes":
        play_mastermind()

if __name__ == "__main__":
    play_mastermind()
