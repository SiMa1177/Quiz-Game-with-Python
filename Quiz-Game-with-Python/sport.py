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

def display_fact(sport: str):
    """Display a fun fact about the sport."""
    facts = {
        "soccer": "Soccer is the most popular sport in the world.",
        "basketball": "Basketball was invented in 1891 by Dr. James Naismith.",
        "tennis": "The fastest recorded serve in tennis was 263 km/h (163.7 mph).",
        "cricket": "Cricket originated in England and is popular in countries like India and Australia.",
        "baseball": "Baseball is known as America's pastime.",
        "hockey": "Ice hockey is played on ice and has its origins in Canada.",
        "golf": "Golf is the only sport to have been played on the moon.",
        "swimming": "Swimming has been a part of the Olympics since the first modern Games in 1896.",
        "volleyball": "Volleyball was invented in 1895 and is now an Olympic sport.",
        "rugby": "Rugby originated in England and is known for its physicality."
    }
    print(f"Fun Fact: {facts.get(sport.lower(), 'No fact available for this sport.')}")

def play_game():
    """Function to run the sport guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the Sports Guessing Game!")
    print("You will have 3 attempts to guess the correct sport.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "Which sport is known as the beautiful game?",
            "answer": "soccer",
            "hint": "This sport is played with a round ball."
        },
        {
            "question": "In which sport do players dribble a ball and shoot it into a hoop?",
            "answer": "basketball",
            "hint": "This sport is popular in the USA."
        },
        {
            "question": "Which sport has singles and doubles matches and is played on a rectangular court?",
            "answer": "tennis",
            "hint": "This sport uses a racket."
        },
        {
            "question": "In which sport do two teams compete to score runs?",
            "answer": "cricket",
            "hint": "This sport is very popular in South Asia."
        },
        {
            "question": "Which sport is played on a diamond with bases?",
            "answer": "baseball",
            "hint": "This sport is often associated with the phrase 'home run.'"
        },
        {
            "question": "Which sport is played on ice with sticks and a puck?",
            "answer": "hockey",
            "hint": "This sport is popular in Canada."
        },
        {
            "question": "Which sport involves hitting a small ball into a series of holes on a course?",
            "answer": "golf",
            "hint": "This sport has a term called 'par.'"
        },
        {
            "question": "Which sport includes events like freestyle and butterfly?",
            "answer": "swimming",
            "hint": "This sport is done in water."
        },
        {
            "question": "Which sport is played with a net and is known for its sets?",
            "answer": "volleyball",
            "hint": "This sport is popular on beaches."
        },
        {
            "question": "Which sport features two teams trying to carry an oval ball across a goal line?",
            "answer": "rugby",
            "hint": "This sport originated in England."
        }
    ]

    random.shuffle(questions)  # Shuffle questions for randomness

    for item in questions:
        guess = input(f"{item['question']} ")
        check_guess(guess, item["answer"], item["hint"])
        display_fact(item["answer"])  # Show a fact after each question
        
        # Ask if the player wants to switch games after each question
        switch_game = input("Do you want to switch to another game? (yes/no): ").strip().lower()
        if switch_game == 'yes':
            return  # Exit play_game to return to the main menu

    print(f"\nYour final score is {score} out of {len(questions)}.")
    if score == len(questions):
        print("Congratulations! You answered all questions correctly!")
    elif score >= len(questions) // 2:
        print("Good job! You know your sports!")
    else:
        print("Better luck next time! Keep learning about sports.")

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

