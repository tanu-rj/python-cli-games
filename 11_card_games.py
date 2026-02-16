"""
Higher or Lower Card Game - Console Version
Guess if the next card will be higher or lower
"""

import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
RANK_VALUES = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
               '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = RANK_VALUES[rank]
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.reset_deck()
    
    def reset_deck(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)
    
    def draw_card(self):
        if len(self.cards) < 10:  # Reset if running low
            self.reset_deck()
        return self.cards.pop()

def play_higher_lower():
    print("=" * 50)
    print("WELCOME TO HIGHER OR LOWER!")
    print("=" * 50)
    print("\nGuess if the next card will be higher or lower")
    print("than the current card.\n")
    
    deck = Deck()
    score = 0
    streak = 0
    max_streak = 0
    
    current_card = deck.draw_card()
    
    while True:
        print(f"Current card: {current_card}")
        print(f"Score: {score} | Streak: {streak} | Best Streak: {max_streak}\n")
        
        guess = input("Is the next card Higher (H) or Lower (L)? (or Q to quit): ").upper().strip()
        
        if guess == "Q":
            break
        
        if guess not in ['H', 'L']:
            print("Invalid input! Enter H or L.\n")
            continue
        
        next_card = deck.draw_card()
        print(f"Next card: {next_card}")
        
        correct = False
        
        if guess == 'H' and next_card.value > current_card.value:
            print("✅ Correct! The next card was higher!")
            correct = True
        elif guess == 'L' and next_card.value < current_card.value:
            print("✅ Correct! The next card was lower!")
            correct = True
        elif next_card.value == current_card.value:
            print("🤝 Same value! It's a push. No points.")
        else:
            print("❌ Wrong! Better luck next time!")
        
        if correct:
            score += 10
            streak += 1
            if streak > max_streak:
                max_streak = streak
        else:
            if streak > 0:
                streak = 0
        
        current_card = next_card
        print()
    
    print("\n" + "=" * 50)
    print("GAME OVER!")
    print(f"Final Score: {score}")
    print(f"Best Streak: {max_streak}")
    print("=" * 50)

def play_lucky_number():
    print("=" * 50)
    print("LUCKY NUMBER CARD GAME!")
    print("=" * 50)
    print("\nYou're dealt 5 cards. The goal is to get the highest")
    print("possible sum without going over 21. Discard and redraw!\n")
    
    deck = Deck()
    total_score = 0
    
    while True:
        print(f"Total Score: {total_score}\n")
        
        # Deal 5 cards
        hand = [deck.draw_card() for _ in range(5)]
        hand_value = sum(card.value for card in hand)
        
        print("Your hand:")
        for i, card in enumerate(hand, 1):
            print(f"{i}. {card} (Value: {card.value})")
        
        print(f"\nHand Sum: {hand_value}")
        
        if hand_value > 21:
            print("❌ Bust! Hand value exceeds 21!")
            continue
        
        print("\nOptions:")
        print("1. Keep this hand")
        print("2. Discard 1 card and draw a new one")
        print("3. Quit")
        
        choice = input("\nChoose (1-3): ").strip()
        
        if choice == "1":
            print(f"✅ You kept a hand worth {hand_value} points!")
            total_score += hand_value
        elif choice == "2":
            card_to_discard = input("Which card to discard (1-5)? ").strip()
            try:
                idx = int(card_to_discard) - 1
                if 0 <= idx < 5:
                    hand[idx] = deck.draw_card()
                    hand_value = sum(card.value for card in hand)
                    print("\nNew hand:")
                    for i, card in enumerate(hand, 1):
                        print(f"{i}. {card}")
                    print(f"Hand Sum: {hand_value}")
                    
                    if hand_value <= 21:
                        print(f"✅ Hand worth {hand_value} points!")
                        total_score += hand_value
                    else:
                        print("❌ Bust! Go again!")
                else:
                    print("Invalid card number!")
                    continue
            except ValueError:
                print("Invalid input!")
                continue
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
            continue
        
        cont = input("\nPlay another hand? (yes/no): ").lower().strip()
        if cont != "yes":
            break
        
        print()
    
    print("\n" + "=" * 50)
    print("GAME OVER!")
    print(f"Final Score: {total_score}")
    print("=" * 50)

if __name__ == "__main__":
    while True:
        print("\nCard Games Menu:")
        print("1. Higher or Lower")
        print("2. Lucky Number")
        print("3. Exit\n")
        
        choice = input("Choose a game (1-3): ").strip()
        
        if choice == "1":
            play_higher_lower()
        elif choice == "2":
            play_lucky_number()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")
