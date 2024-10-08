import random

# Global variable to keep track of the score
score = 0

def check_guess(guess: str, answer: str, hint: str):
    """Check the player's guess against the correct answer."""
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer!")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                print(f"Sorry, wrong answer. Hint: {hint}")
                guess = input("Try again: ")
            attempt += 1

    if attempt == 3:
        print(f"The correct answer is {answer}.")

def display_fact(fruit: str):
    """Display a fun fact about the fruit."""
    facts = {
        "apple": "Apples are 25% air, which is why they float.",
        "banana": "Bananas are berries, but strawberries are not.",
        "grape": "There are over 8,000 varieties of grapes worldwide.",
        "orange": "Oranges are a great source of vitamin C.",
        "strawberry": "Strawberries have seeds on the outside, not the inside.",
        "watermelon": "Watermelon is 92% water.",
        "pineapple": "Pineapples can take up to two years to grow.",
        "kiwi": "Kiwis are high in vitamin C and vitamin K.",
        "mango": "Mangoes are the national fruit of India.",
        "peach": "Peaches are a member of the rose family."
    }
    print(f"Fun Fact: {facts.get(fruit.lower(), 'No fact available for this fruit.')}")

def play_game():
    """Function to run the fruit guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the Fruit Guessing Game!")
    print("You will have 3 attempts to guess the correct fruit.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "Which fruit is known for keeping the doctor away if you eat one a day?",
            "answer": "apple",
            "hint": "This fruit is often red or green."
        },
        {
            "question": "Which fruit is known for being curved and yellow?",
            "answer": "banana",
            "hint": "Monkeys are known to love this fruit."
        },
        {
            "question": "Which fruit is small, round, and often used in wine production?",
            "answer": "grape",
            "hint": "This fruit comes in green, red, and black varieties."
        },
        {
            "question": "Which fruit is a citrus and is often used in juices?",
            "answer": "orange",
            "hint": "This fruit is a good source of vitamin C."
        },
        {
            "question": "Which fruit has seeds on the outside?",
            "answer": "strawberry",
            "hint": "This fruit is often used in desserts."
        },
        {
            "question": "Which fruit is known for its high water content and is often enjoyed in summer?",
            "answer": "watermelon",
            "hint": "This fruit is typically green on the outside."
        },
        {
            "question": "Which tropical fruit can take up to two years to grow?",
            "answer": "pineapple",
            "hint": "This fruit is known for its spiky exterior."
        },
        {
            "question": "Which fruit is brown on the outside and green on the inside?",
            "answer": "kiwi",
            "hint": "This fruit is high in vitamin C."
        },
        {
            "question": "Which fruit is the national fruit of India?",
            "answer": "mango",
            "hint": "This fruit is known for its sweet and juicy flesh."
        },
        {
            "question": "Which fruit is often found in pies and is a member of the rose family?",
            "answer": "peach",
            "hint": "This fruit has fuzzy skin."
        }
    ]

    random.shuffle(questions)  # Shuffle questions for randomness

    for item in questions:
        guess = input(f"{item['question']} ")
        check_guess(guess, item["answer"], item["hint"])
        display_fact(item["answer"])  # Show a fact after each question

        # Ask if the player wants to switch games
        switch_game = input("Do you want to switch to another game? (yes/no): ").strip().lower()
        if switch_game == 'yes':
            return  # Exit play_game to return to the main menu

    print(f"\nYour final score is {score} out of {len(questions)}.")
    if score == len(questions):
        print("Congratulations! You answered all questions correctly!")
    elif score >= len(questions) // 2:
        print("Good job! You know your fruits!")
    else:
        print("Better luck next time! Keep learning about fruits.")

def main():
    """Main function to execute the game."""
    while True:
        play_game()
        play_again = input("Would you like to play again? (yes/no) ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
