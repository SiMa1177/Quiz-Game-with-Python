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

def display_fact(city: str):
    """Display a fun fact about the city."""
    facts = {
        "paris": "Paris is known as the City of Light.",
        "tokyo": "Tokyo is the most populous city in the world.",
        "new york": "New York is known as the Big Apple.",
        "london": "London is famous for the Tower of London and Buckingham Palace.",
        "berlin": "Berlin is known for its art scene and modern landmarks.",
        "sydney": "Sydney is famous for its Opera House and Harbour Bridge.",
        "mumbai": "Mumbai is the financial capital of India.",
        "cairo": "Cairo is home to the Great Pyramids of Giza.",
        "rome": "Rome is known for its nearly 3,000 years of globally influential art, architecture, and culture.",
        "rio de janeiro": "Rio de Janeiro is famous for its Carnival festival."
    }
    print(f"Fun Fact: {facts.get(city.lower(), 'No fact available for this city.')}")

def play_game():
    """Function to run the city guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the City Guessing Game!")
    print("You will have 3 attempts to guess the correct city.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "Which city is known as the City of Light?",
            "answer": "paris",
            "hint": "This city is famous for the Eiffel Tower."
        },
        {
            "question": "Which city is the most populous in the world?",
            "answer": "tokyo",
            "hint": "This city is located in Japan."
        },
        {
            "question": "Which city is known as the Big Apple?",
            "answer": "new york",
            "hint": "This city is located in the USA."
        },
        {
            "question": "Which city is famous for the Tower of London?",
            "answer": "london",
            "hint": "This city is the capital of England."
        },
        {
            "question": "Which city is known for its art scene and modern landmarks?",
            "answer": "berlin",
            "hint": "This city is the capital of Germany."
        },
        {
            "question": "Which city is famous for its Opera House?",
            "answer": "sydney",
            "hint": "This city is located in Australia."
        },
        {
            "question": "Which city is the financial capital of India?",
            "answer": "mumbai",
            "hint": "This city is known for Bollywood."
        },
        {
            "question": "Which city is home to the Great Pyramids of Giza?",
            "answer": "cairo",
            "hint": "This city is located in Egypt."
        },
        {
            "question": "Which city is known for its nearly 3,000 years of globally influential art, architecture, and culture?",
            "answer": "rome",
            "hint": "This city is the capital of Italy."
        },
        {
            "question": "Which city is famous for its Carnival festival?",
            "answer": "rio de janeiro",
            "hint": "This city is located in Brazil."
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
        print("Good job! You know your cities!")
    else:
        print("Better luck next time! Keep learning about cities.")

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