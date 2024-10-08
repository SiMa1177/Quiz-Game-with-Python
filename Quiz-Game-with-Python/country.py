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

def display_fact(country: str):
    """Display a fun fact about the country."""
    facts = {
        "canada": "Canada has the longest coastline of any country in the world.",
        "brazil": "Brazil is the largest country in South America.",
        "australia": "Australia is both a country and a continent.",
        "france": "France is famous for its art, fashion, and cuisine.",
        "japan": "Japan is an island nation located in East Asia.",
        "india": "India is the second-most populous country in the world.",
        "egypt": "Egypt is home to the ancient pyramids and the Nile River.",
        "germany": "Germany is known for its history, culture, and engineering.",
        "south africa": "South Africa is known for its diverse ecosystems and wildlife.",
        "usa": "The United States is made up of 50 states and is known for its cultural diversity."
    }
    print(f"Fun Fact: {facts.get(country.lower(), 'No fact available for this country.')}")

def play_game():
    """Function to run the country guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the Country Guessing Game!")
    print("You will have 3 attempts to guess the correct country.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "Which country is known for its maple syrup?",
            "answer": "canada",
            "hint": "It has a famous city called Toronto."
        },
        {
            "question": "Which country is the largest in South America?",
            "answer": "brazil",
            "hint": "It is famous for the Amazon rainforest."
        },
        {
            "question": "Which country is both a country and a continent?",
            "answer": "australia",
            "hint": "It is known for its unique wildlife."
        },
        {
            "question": "Which country is famous for the Eiffel Tower?",
            "answer": "france",
            "hint": "It is known for its rich history in art and culture."
        },
        {
            "question": "Which country is an island nation located in East Asia?",
            "answer": "japan",
            "hint": "It is known for its technology and cherry blossoms."
        },
        {
            "question": "Which country is the second-most populous in the world?",
            "answer": "india",
            "hint": "It is known for its diverse culture and languages."
        },
        {
            "question": "Which country is home to the ancient pyramids?",
            "answer": "egypt",
            "hint": "It is located in North Africa."
        },
        {
            "question": "Which country is known for its beer and Oktoberfest?",
            "answer": "germany",
            "hint": "It has a rich history and cultural heritage."
        },
        {
            "question": "Which country is known for its wildlife and the Big Five?",
            "answer": "south africa",
            "hint": "It is famous for its national parks."
        },
        {
            "question": "Which country is made up of 50 states?",
            "answer": "usa",
            "hint": "It is known for its cultural diversity and landmarks."
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
        print("Good job! You know your countries!")
    else:
        print("Better luck next time! Keep learning about countries.")

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