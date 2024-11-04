# Import the tkinter library for creating GUI applications
import tkinter as tk
from tkinter import messagebox

# Import the Hangman class (assumed to be in a separate module 'hangman.py') which handles the game logic
from hangman import Hangman

# Define a class for the Hangman game application
class HangmanApp:
    # Initialize the HangmanApp with the root window and a list of words for the game
    def __init__(self, root, word_list):
        # Create an instance of the Hangman game logic using the provided word list
        self.game = Hangman(word_list)
        # Store the root Tkinter window
        self.root = root
        # Set the title of the root window
        self.root.title("Hangman Game")
        # Call the method to create all the widgets for the GUI
        self.create_widgets()

    # Method to create and display all widgets for the Hangman game
    def create_widgets(self):
        # Display the current state of the word with guessed letters and underscores for unguessed letters
        self.word_label = tk.Label(self.root, text=self.game.display_word(), font=("Helvetica", 18))
        self.word_label.pack(pady=10)# Add some vertical padding

        # Display the number of incorrect guesses remaining
        self.info_label = tk.Label(self.root, text=f"Incorrect guesses remaining: {self.game.remaining_attempts()}", font=("Helvetica", 12))
        self.info_label.pack(pady=5)

        # Create an entry box for the player to type in their letter guess
        self.letter_entry = tk.Entry(self.root, font=("Helvetica", 14), width=5)
        self.letter_entry.pack(pady=5)

        # Create a button to submit the player's guess
        self.guess_button = tk.Button(self.root, text="Guess", command=self.guess_letter)
        self.guess_button.pack(pady=5)

        # Create a button to reset the game and start a new round
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5)

    # Method to handle letter guesses made by the player
    def guess_letter(self):
        # Get the letter input by the player, and strip any surrounding whitespace
        guess = self.letter_entry.get().strip().lower()
        # Clear the entry box after taking the guess
        self.letter_entry.delete(0, tk.END)

        # Validate the input to make sure it's a single alphabetical letter
        if len(guess) != 1 or not guess.isalpha():
            # Show a warning if the input is invalid
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        # Check if the letter has already been guessed
        if not self.game.guess_letter(guess):
            # Inform the player if they've already guessed this letter
            messagebox.showinfo("Info", "You already guessed that letter!")
            return

        # Update the game display with the current game state
        self.update_game_status()

        # Check if the player has guessed the entire word
        if self.game.is_word_guessed():
            # Congratulate the player if they guessed the word correctly
            messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.game.secret_word}")
            # End the game to prevent further guesses
            self.end_game()

        # Check if the player has run out of guesses
        if self.game.remaining_attempts() == 0:
            # Inform the player of game over and reveal the correct word
            messagebox.showinfo("Game Over", f"You've run out of guesses. The word was: {self.game.secret_word}")
            # End the game to prevent further guesses
            self.end_game()

    # Method to update the display of the word and remaining attempts
    def update_game_status(self):
        # Update the word label to show the current guessed letters and remaining blanks
        self.word_label.config(text=self.game.display_word())
        # Update the information label to show remaining incorrect guesses
        self.info_label.config(text=f"Incorrect guesses remaining: {self.game.remaining_attempts()}")

    # Method to end the game by disabling input controls
    def end_game(self):
        # Disable the letter entry box
        self.letter_entry.config(state=tk.DISABLED)
        # Disable the guess button
        self.guess_button.config(state=tk.DISABLED)

    # Method to reset the game to a new round
    def reset_game(self):
        # Reinitialize the game with a new instance of Hangman and a fresh word list
        self.game = Hangman(["python", "hangman", "challenge", "programming", "developer", "console", "game"])
        # Update the display to the initial state for the new game
        self.update_game_status()
        # Enable the letter entry box for new guesses
        self.letter_entry.config(state=tk.NORMAL)
        # Enable the guess button
        self.guess_button.config(state=tk.NORMAL)

# Main block to run the application
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Create an instance of HangmanApp with the root window and a list of words
    app = HangmanApp(root, ["python", "hangman", "challenge", "programming", "developer", "console", "game"])
    # Start the Tkinter main event loop
    root.mainloop()
