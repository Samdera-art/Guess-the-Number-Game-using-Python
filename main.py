import random

# List to store attempts for high score
attempts_list = []

# Function to display the current high score
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

# Main game function
def start_game():
    random_number = random.randint(1, 30)
    print("Hey There! Welcome to the game of guesses!")
    player_name = input("Enter your name: ")
    wanna_play = input(f"Hi {player_name}, would you like to play the guessing game? (Enter Yes/No): ")

    attempts = 0
    show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 30: ")
            if int(guess) < 1 or int(guess) > 30:
                raise ValueError("Please guess a number within the range of 1 to 30.")

            attempts += 1
            if int(guess) == random_number:
                print("Congrats! You guessed it right!")
                print(f"It took you {attempts} attempts.")
                attempts_list.append(attempts)
                play_again = input("Would you like to play again? (Enter Yes/No): ")
                if play_again.lower() == "no":
                    print("That's cool, have a nice day!")
                    break
                else:
                    attempts = 0
                    random_number = random.randint(1, 30)
                    show_score()
            elif int(guess) < random_number:
                print("It's higher!")
            elif int(guess) > random_number:
                print("It's lower!")
        except ValueError as err:
            print("Oh!, that is not a valid input. Try again...")
            print(f"({err})")
    else:
        print("That's cool, have a nice day!")

# Entry point of the program
if __name__ == '__main__':
    start_game()
