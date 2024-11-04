# Import the Hangman class from hangman.py
from hangman import Hangman

# Main function to run the Hangman game
def main():
    # List of words for the Hangman game
    words = ["python", "hangman", "challenge", "programming", "developer", "console", "game"]
    
    # Create an instance of the Hangman game
    game = Hangman(words)

    # Initial game instructions
    print("Welcome to Hangman!")
    print(f"You have {game.remaining_attempts()} incorrect guesses available.")
    print("Good luck!")

    # Main game loop, runs until the game is over
    while not game.is_game_over():
        # Display the current state of the guessed word
        print("\nCurrent word: ", game.display_word())
        # Show remaining incorrect guesses
        print(f"Incorrect guesses remaining: {game.remaining_attempts()}")
        # Prompt player for a letter
        guess = input("Guess a letter: ").strip().lower()

        # Check if input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue  # Skip to the next iteration if input is invalid

        # Attempt to guess the letter and update game state
        if not game.guess_letter(guess):
            continue  # If guess is invalid or already guessed, skip to the next iteration

        # Check if the word has been fully guessed
        if game.is_word_guessed():
            print("\nCongratulations! You've guessed the word:", game.secret_word)
            break  # End the game if the word is correctly guessed

    # End-of-game message for when the player has run out of guesses
    if game.incorrect_guesses >= game.max_attempts:
        print("\nGame Over! You've run out of guesses.")
        print("The word was:", game.secret_word)

# Check if this script is being run directly
if __name__ == "__main__":
    main() # Call the main function to start the game
