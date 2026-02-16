"""
Quiz Game - Test Your Knowledge
Multiple choice quiz with scoring
"""

import random

QUIZ_DATA = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Saturn", "Jupiter", "Neptune", "Uranus"],
        "correct": 1
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"],
        "correct": 2
    },
    {
        "question": "What year did the Titanic sink?",
        "options": ["1912", "1915", "1920", "1905"],
        "correct": 0
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "correct": 2
    },
    {
        "question": "Which country is home to the Statue of Liberty?",
        "options": ["UK", "USA", "France", "Germany"],
        "correct": 1
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "correct": 2
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Venus", "Mercury", "Earth", "Mars"],
        "correct": 1
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct": 1
    },
    {
        "question": "In what year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "correct": 2
    }
]

def play_quiz():
    print("=" * 50)
    print("WELCOME TO QUIZ GAME!")
    print("=" * 50)
    
    quiz = random.sample(QUIZ_DATA, min(5, len(QUIZ_DATA)))
    score = 0
    
    for i, question_data in enumerate(quiz, 1):
        print(f"\n{'=' * 50}")
        print(f"Question {i}/5")
        print(f"{'=' * 50}")
        print(question_data["question"])
        print()
        
        for j, option in enumerate(question_data["options"], 1):
            print(f"{j}. {option}")
        
        while True:
            try:
                answer = int(input("\nYour answer (1-4): ")) - 1
                
                if answer < 0 or answer > 3:
                    print("Please enter a number between 1 and 4!")
                    continue
                
                if answer == question_data["correct"]:
                    print("✅ Correct!")
                    score += 1
                else:
                    correct_answer = question_data["options"][question_data["correct"]]
                    print(f"❌ Wrong! The correct answer is: {correct_answer}")
                
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    print(f"\n{'=' * 50}")
    print(f"QUIZ COMPLETE!")
    print(f"{'=' * 50}")
    print(f"Your score: {score}/5")
    
    percentage = (score / 5) * 100
    if percentage == 100:
        print("🏆 Perfect score! You're a genius!")
    elif percentage >= 80:
        print("🥇 Excellent! Great knowledge!")
    elif percentage >= 60:
        print("🥈 Good! You know your stuff!")
    elif percentage >= 40:
        print("🥉 Not bad! Keep learning!")
    else:
        print("💪 Keep studying and try again!")
    
    if input("\nTake the quiz again? (yes/no): ").lower() == "yes":
        play_quiz()

if __name__ == "__main__":
    play_quiz()
