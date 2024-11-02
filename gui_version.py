import tkinter as tk
from tkinter import messagebox
import random

# Predefined list of words
WORDS = ["python", "java", "programming", "hangman", "developer", "software", "keyboard"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.word_to_guess = random.choice(WORDS)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        self.all_guessed_letters = set()
        
        self.word_display = tk.StringVar()
        self.guess_entry = tk.StringVar()

        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text="Hangman Game", font=("Arial", 16)).pack(pady=10)
        
        self.update_word_display()

        tk.Label(self.root, textvariable=self.word_display, font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Enter a letter:").pack()

        tk.Entry(self.root, textvariable=self.guess_entry, font=("Arial", 14)).pack(pady=5)
        tk.Button(self.root, text="Guess", command=self.check_guess, font=("Arial", 12)).pack(pady=10)

        self.incorrect_label = tk.Label(self.root, text=f"Incorrect guesses remaining: {self.max_incorrect_guesses}", font=("Arial", 12))
        self.incorrect_label.pack(pady=5)
        
        self.guessed_label = tk.Label(self.root, text="Guessed letters: ", font=("Arial", 12))
        self.guessed_label.pack(pady=5)

    def update_word_display(self):
        self.word_display.set(" ".join([letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess]))

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.set("")

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.all_guessed_letters:
            messagebox.showwarning("Already Guessed", f"You've already guessed '{guess}'. Try a different letter.")
            return

        self.all_guessed_letters.add(guess)

        if guess in self.word_to_guess:
            self.guessed_letters.add(guess)
            self.update_word_display()
        else:
            self.incorrect_guesses += 1
            self.incorrect_label.config(text=f"Incorrect guesses remaining: {self.max_incorrect_guesses - self.incorrect_guesses}")

        self.guessed_label.config(text=f"Guessed letters: {' '.join(sorted(self.all_guessed_letters))}")

        # Check if the game is won or lost
        if all([letter in self.guessed_letters for letter in self.word_to_guess]):
            messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.word_to_guess}")
            self.reset_game()
        elif self.incorrect_guesses >= self.max_incorrect_guesses:
            messagebox.showinfo("Game Over", f"Game over! The word was: {self.word_to_guess}")
            self.reset_game()

    def reset_game(self):
        self.word_to_guess = random.choice(WORDS)
        self.guessed_letters = set()
        self.all_guessed_letters = set()
        self.incorrect_guesses = 0
        self.incorrect_label.config(text=f"Incorrect guesses remaining: {self.max_incorrect_guesses}")
        self.guessed_label.config(text="Guessed letters: ")
        self.update_word_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
