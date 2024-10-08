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

def display_fact(planet: str):
    """Display a fun fact about the planet."""
    facts = {
        "mercury": "Mercury is the closest planet to the Sun and has no atmosphere.",
        "venus": "Venus is the hottest planet in our solar system.",
        "earth": "Earth is the only planet known to support life.",
        "mars": "Mars is known as the Red Planet due to iron oxide on its surface.",
        "jupiter": "Jupiter is the largest planet in our solar system.",
        "saturn": "Saturn is famous for its stunning rings.",
        "uranus": "Uranus rotates on its side, making it unique among planets.",
        "neptune": "Neptune is known for its strong winds and dark blue color.",
        "pluto": "Pluto was reclassified as a dwarf planet in 2006.",
        "planet x": "Planet X is a hypothetical planet in the outer solar system."
    }
    print(f"Fun Fact: {facts.get(planet.lower(), 'No fact available for this planet.')}")

def play_game():
    """Function to run the planet guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the Planet Guessing Game!")
    print("You will have 3 attempts to guess the correct planet.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "Which planet is closest to the Sun?",
            "answer": "mercury",
            "hint": "This planet has no atmosphere."
        },
        {
            "question": "Which planet is known as the hottest planet?",
            "answer": "venus",
            "hint": "This planet is often called Earth's sister planet."
        },
        {
            "question": "Which planet is known for its water and life?",
            "answer": "earth",
            "hint": "This is the third planet from the Sun."
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "answer": "mars",
            "hint": "This planet has a reddish appearance."
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "answer": "jupiter",
            "hint": "This planet is a gas giant."
        },
        {
            "question": "Which planet is famous for its rings?",
            "answer": "saturn",
            "hint": "This planet is the sixth from the Sun."
        },
        {
            "question": "Which planet rotates on its side?",
            "answer": "uranus",
            "hint": "This planet has a unique tilt."
        },
        {
            "question": "Which planet is known for its strong winds?",
            "answer": "neptune",
            "hint": "This is the eighth planet from the Sun."
        },
        {
            "question": "Which dwarf planet was reclassified in 2006?",
            "answer": "pluto",
            "hint": "This planet is now considered a dwarf planet."
        },
        {
            "question": "What is the hypothetical planet in the outer solar system?",
            "answer": "planet x",
            "hint": "This is a name given to a possible undiscovered planet."
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
        print("Good job! You know your planets!")
    else:
        print("Better luck next time! Keep learning about planets.")

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
