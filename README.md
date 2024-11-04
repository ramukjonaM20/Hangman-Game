# Hangman-Challenge
A classic Hangman game where players try to guess a hidden word, one letter at a time, with a limited number of attempts. The game displays the current state of the word, tracks incorrect guesses, and ends with either a win or a loss. Developed in Python, this project can be run in the console and can be expanded to include a graphical user interface (GUI) using Tkinter or PyQt.
## Table of Contents
* [Project Description](#project-description)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [How to Play](#how-to-play)
* [Future Enhancements](#future-enhancements)
## Project Description
The "Hangman Challenge" project recreates the traditional word-guessing game in Python. A random word is selected from a predefined list, and the player attempts to guess the word by entering one letter at a time. The game tracks the player’s correct guesses, displays the word's current state, and allows for a limited number of incorrect attempts before the game is over. The project starts as a console-based application but can be extended to a GUI for a more user-friendly experience.
## Features
* **Word Selection:** Randomly selects a word from a predefined list.
* **Player Input:** Allows players to input their guesses, checking if each letter is correct.
* **Game State Display:** Shows the current state of the word with guessed letters revealed and unguessed letters blanked.
* **Incorrect Guess Tracking:** Displays the number of remaining incorrect guesses and keeps track of guessed letters.
* **Win/Loss Conditions:** Ends the game when the player either guesses the word or exhausts their attempts.
* **Optional GUI:** An optional GUI can be added using Tkinter or PyQt to improve user interaction.
## Technologies Used
* **Python:** For core game logic and functionality.
* **Tkinter/PyQt (Optional):** To build a graphical interface, if desired.
## How to Play
1. The game randomly selects a word from a list.
2. You have a limited number of attempts to guess the word.
3. Input a single letter at a time to guess the word:
    * If the letter is in the word, it will appear in the current word display.
    * If the letter is incorrect, your remaining attempts will decrease.
4. The game ends when:
    * You correctly guess all letters in the word (win).
    * You run out of attempts (lose).
## Future Enhancements
Possible upgrades for this project include:
* **Additional Word Lists:** Add a larger or more varied list of words for replayability.
* **Difficulty Levels:** Adjust the number of attempts based on difficulty settings (e.g., easy, medium, hard).
* **Hint System:** Add hints to help players guess the word.
* **Advanced GUI:** Develop a more feature-rich GUI using Tkinter or PyQt for improved usability.
Score Tracking: Keep track of wins and losses across sessions.
