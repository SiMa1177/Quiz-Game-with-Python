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

def display_fact(movie: str):
    """Display a fun fact about the movie."""
    facts = {
        "inception": "Inception features a dream within a dream concept.",
        "avatar": "Avatar was the first film to gross over $2 billion.",
        "titanic": "Titanic won 11 Academy Awards and is one of the highest-grossing films.",
        "the godfather": "The Godfather is considered one of the greatest films of all time.",
        "the dark knight": "Heath Ledger won a posthumous Oscar for his role as the Joker.",
        "pulp fiction": "Pulp Fiction revitalized John Travolta's career.",
        "the shawshank redemption": "The Shawshank Redemption is frequently rated as the best movie on IMDb.",
        "star wars": "Star Wars is one of the most successful franchises in film history.",
        "forrest gump": "Forrest Gump is famous for the quote 'Life is like a box of chocolates.'",
        "gladiator": "Gladiator won the Academy Award for Best Picture in 2001."
    }
    print(f"Fun Fact: {facts.get(movie.lower(), 'No fact available for this movie.')}")

def play_game():
    """Function to run the movie guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the Movie Guessing Game!")
    print("You will have 3 attempts to guess the correct movie.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "Which movie features a dream within a dream?",
            "answer": "inception",
            "hint": "This film stars Leonardo DiCaprio."
        },
        {
            "question": "Which film was the first to gross over $2 billion?",
            "answer": "avatar",
            "hint": "This film is set on a distant moon."
        },
        {
            "question": "Which film won 11 Academy Awards?",
            "answer": "titanic",
            "hint": "This movie is about a sinking ship."
        },
        {
            "question": "Which movie is considered one of the greatest of all time?",
            "answer": "the godfather",
            "hint": "This film features the Corleone family."
        },
        {
            "question": "In which movie did Heath Ledger play the Joker?",
            "answer": "the dark knight",
            "hint": "This film is part of the Batman franchise."
        },
        {
            "question": "Which film revitalized John Travolta's career?",
            "answer": "pulp fiction",
            "hint": "This movie is known for its non-linear storytelling."
        },
        {
            "question": "Which movie is frequently rated as the best on IMDb?",
            "answer": "the shawshank redemption",
            "hint": "This film is about hope and friendship."
        },
        {
            "question": "Which franchise features characters like Luke Skywalker?",
            "answer": "star wars",
            "hint": "This film is set in a galaxy far, far away."
        },
        {
            "question": "Which movie features the quote 'Life is like a box of chocolates'?",
            "answer": "forrest gump",
            "hint": "This film stars Tom Hanks."
        },
        {
            "question": "Which movie won the Academy Award for Best Picture in 2001?",
            "answer": "gladiator",
            "hint": "This film is about a Roman general turned gladiator."
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
        print("Good job! You know your movies!")
    else:
        print("Better luck next time! Keep learning about movies.")

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
