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

def display_fact(food: str):
    """Display a fun fact about the food."""
    facts = {
        "pizza": "Pizza was invented in Naples, Italy.",
        "sushi": "Sushi originally started as a way to preserve fish in fermented rice.",
        "burger": "The hamburger was created in Germany but became popular in the U.S.",
        "pasta": "Pasta is said to have been brought to Italy from China by Marco Polo.",
        "taco": "Tacos originated in Mexico and are often filled with meat, cheese, and vegetables.",
        "ice cream": "Ice cream has been enjoyed for centuries, dating back to ancient China.",
        "salad": "Salads can be made from a variety of ingredients, including vegetables, fruits, and nuts.",
        "cake": "The world's largest cake was made in 2006 and weighed over 8,000 pounds.",
        "chocolate": "Chocolate was used as currency in ancient Mesoamerica.",
        "popcorn": "Popcorn has been around for thousands of years and was used in ancient Peru."
    }
    print(f"Fun Fact: {facts.get(food.lower(), 'No fact available for this food.')}")

def play_game():
    """Function to run the food guessing game."""
    global score  # Ensure to use the global score
    score = 0  # Reset score for each game
    print("Welcome to the Food Guessing Game!")
    print("You will have 3 attempts to guess the correct food.")
    print("Let's get started!\n")

    questions = [
        {
            "question": "What is a popular Italian dish made of dough topped with sauce and cheese?",
            "answer": "pizza",
            "hint": "It is often round and baked in an oven."
        },
        {
            "question": "What Japanese dish consists of vinegared rice accompanied by various ingredients?",
            "answer": "sushi",
            "hint": "It can include seafood, vegetables, and sometimes tropical fruits."
        },
        {
            "question": "What is a sandwich consisting of a cooked patty of ground meat?",
            "answer": "burger",
            "hint": "It is often served in a bun with toppings."
        },
        {
            "question": "What type of food is made from unleavened dough, often associated with Italian cuisine?",
            "answer": "pasta",
            "hint": "It is commonly served with sauce."
        },
        {
            "question": "What is a traditional Mexican dish that consists of a folded or rolled tortilla?",
            "answer": "taco",
            "hint": "It can be filled with meat, beans, cheese, and vegetables."
        },
        {
            "question": "What sweetened frozen food is often made from cream or milk?",
            "answer": "ice cream",
            "hint": "It is a popular dessert in many cultures."
        },
        {
            "question": "What dish is often made with a mixture of leafy greens, vegetables, and dressings?",
            "answer": "salad",
            "hint": "It can be served as a side dish or main course."
        },
        {
            "question": "What sweet baked food is often layered and frosted?",
            "answer": "cake",
            "hint": "It is commonly served at celebrations."
        },
        {
            "question": "What treat is made from roasted and ground cacao beans?",
            "answer": "chocolate",
            "hint": "It is often sweet and used in desserts."
        },
        {
            "question": "What is a type of corn kernel that pops when heated?",
            "answer": "popcorn",
            "hint": "It is a popular snack at movies."
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
        print("Good job! You know your foods!")
    else:
        print("Better luck next time! Keep learning about foods.")

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
