# main.py

import animal
import city
import country
import food
import fruit
import movie
import planet
import sport

def main():
    """Main function to run the application."""
    print("Welcome to the Quiz Application!")

    while True:
        print("\nChoose a game to play:")
        print("1. Animal Guessing Game")
        print("2. City Guessing Game")
        print("3. Country Guessing Game")
        print("4. Food Guessing Game")
        print("5. Fruit Guessing Game")
        print("6. Movie Guessing Game")
        print("7. Planet Guessing Game")
        print("8. Sport Guessing Game")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            animal.play_game()  # Call play_game from animal.py
        elif choice == '2':
            city.play_game()  # Call play_game from city.py
        elif choice == '3':
            country.play_game()  # Call play_game from country.py
        elif choice == '4':
            food.play_game()  # Call play_game from food.py
        elif choice == '5':
            fruit.play_game()  # Call play_game from fruit.py
        elif choice == '6':
            movie.play_game()  # Call play_game from movie.py
        elif choice == '7':
            planet.play_game()  # Call play_game from planet.py
        elif choice == '8':
            sport.play_game()  # Call play_game from sport.py
        elif choice == '9':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
