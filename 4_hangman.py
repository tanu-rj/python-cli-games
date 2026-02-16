"""
Hangman Game
Guess the word before running out of attempts
"""

import random

WORD_LIST = [
    "python", "hangman", "computer", "programming", "keyboard", "monitor",
    "algorithm", "database", "function", "variable", "internet", "website",
    "software", "hardware", "network", "application", "developer", "server",
    "browser", "password"
]

HANGMAN_STAGES = [
    "❌❌❌❌❌❌\n❌      ❌\n❌      ❌\n❌",
    "❌❌❌❌❌❌\n❌      ❌\n❌      O\n❌",
    "❌❌❌❌❌❌\n❌      ❌\n❌      O\n❌      |\n❌",
    "❌❌❌❌❌❌\n❌      ❌\n❌      O\n❌     \\|/\n❌",
    "❌❌❌❌❌❌\n❌      ❌\n❌      O\n❌     \\|/\n❌      |\n❌",
    "❌❌❌❌❌❌\n❌      ❌\n❌      O\n❌     \\|/\n❌      |\n❌     / |",
    "❌❌❌❌❌❌\n❌      ❌\n❌      O\n❌     \\|/\n❌      |\n❌     / \\"
]

def play_hangman():
    print("=" * 50)
    print("WELCOME TO HANGMAN!")
    print("=" * 50)
    
    word = random.choice(WORD_LIST).upper()
    word_display = ["_"] * len(word)
    guessed_letters = set()
    wrong_guesses = set()
    attempts_left = 6
    
    print(f"\nThe word has {len(word)} letters.\n")
    
    while attempts_left > 0 and "_" in word_display:
        print(HANGMAN_STAGES[6 - attempts_left])
        print(f"\nWord: {' '.join(word_display)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
        print(f"Attempts left: {attempts_left}\n")
        
        guess = input("Guess a letter: ").upper().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!\n")
            continue
        
        if guess in guessed_letters or guess in wrong_guesses:
            print("❌ You already guessed that letter!\n")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
            print(f"✅ Good guess! '{guess}' is in the word!\n")
        else:
            wrong_guesses.add(guess)
            attempts_left -= 1
            print(f"❌ Sorry, '{guess}' is not in the word!\n")
    
    print(HANGMAN_STAGES[6 - attempts_left])
    
    if "_" not in word_display:
        print(f"\n🎉 Congratulations! You won! The word is: {word}")
    else:
        print(f"\n💀 Game Over! The word was: {word}")
    
    if input("\nPlay again? (yes/no): ").lower() == "yes":
        play_hangman()

if __name__ == "__main__":
    play_hangman()
