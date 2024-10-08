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

def display_fact(animal: str):
    """Display a fun fact about the animal."""
    facts = {
        "lion": "Lions are known as the kings of the jungle.",
        "elephant": "Elephants are the largest land animals on Earth.",
        "giraffe": "Giraffes have the longest necks of any animal.",
        "dolphin": "Dolphins are known for their intelligence and playful behavior.",
        "penguin": "Penguins are flightless birds that are excellent swimmers.",
        "kangaroo": "Kangaroos are native to Australia and can jump great distances.",
        "tiger": "Tigers are the largest species of cat and are known for their striking stripes.",
        "zebra": "Zebras are known for their black and white striped coats.",
        "bear": "Bears are known for their strength and can hibernate in winter.",
        "shark": "Sharks are some of the most efficient predators in the ocean."
    }
    print(f"Fun Fact: {facts.get(animal.lower(), 'No fact available for this animal.')}")

def play_game():
    """Function to run the animal guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the Animal Guessing Game!")
    print("You will have 3 attempts to guess the correct animal.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "Which animal is known as the king of the jungle?",
            "answer": "lion",
            "hint": "This animal is known for its mane."
        },
        {
            "question": "Which animal is the largest land animal on Earth?",
            "answer": "elephant",
            "hint": "This animal has a trunk."
        },
        {
            "question": "Which animal has the longest neck of any animal?",
            "answer": "giraffe",
            "hint": "This animal is known for reaching high trees."
        },
        {
            "question": "Which animal is known for its intelligence and playful behavior?",
            "answer": "dolphin",
            "hint": "This animal lives in the ocean."
        },
        {
            "question": "Which animal is a flightless bird that is an excellent swimmer?",
            "answer": "penguin",
            "hint": "This animal lives in cold regions."
        },
        {
            "question": "Which animal is native to Australia and can jump great distances?",
            "answer": "kangaroo",
            "hint": "This animal carries its young in a pouch."
        },
        {
            "question": "Which animal is the largest species of cat and is known for its striking stripes?",
            "answer": "tiger",
            "hint": "This animal is a solitary hunter."
        },
        {
            "question": "Which animal is known for its black and white striped coat?",
            "answer": "zebra",
            "hint": "This animal is often found in Africa."
        },
        {
            "question": "Which animal is known for its strength and can hibernate in winter?",
            "answer": "bear",
            "hint": "This animal can be found in forests."
        },
        {
            "question": "Which animal is one of the most efficient predators in the ocean?",
            "answer": "shark",
            "hint": "This animal has many species, including great white."
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
        print("Good job! You know your animals!")
    else:
        print("Better luck next time! Keep learning about animals.")

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
