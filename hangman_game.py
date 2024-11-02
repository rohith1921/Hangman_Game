import random

# Predefined list of words for the game
WORDS = ["python", "java", "programming", "hangman", "developer", "software", "keyboard"]

# Function to choose a random word
def choose_word():
    return random.choice(WORDS)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Main Hangman game function
def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    all_guessed_letters = set()

    print("\nWelcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters so far: {' '.join(sorted(all_guessed_letters))}")

        # Get player input
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in all_guessed_letters:
            print(f"You have already guessed '{guess}'. Try a different letter.")
            continue

        all_guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        # Check if the player has guessed the entire word
        if all([letter in guessed_letters for letter in word_to_guess]):
            print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nGame over! You've run out of guesses. The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()
