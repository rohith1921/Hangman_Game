# Hangman Game 🎮

A classic Hangman game built in Python. The game selects a random word, and players attempt to guess it letter by letter. Includes features such as a limited number of attempts, visual representation of the Hangman, and an optional GUI for improved user experience.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Random Word Selection**: Each game starts with a randomly chosen word.
- **Player Input**: Allows players to guess one letter at a time.
- **Limited Attempts**: Players have a set number of attempts before losing the game.
- **Game State Display**: Shows the current state of the word and incorrect guesses.
- **Win/Loss Conditions**: The game ends when the word is guessed or attempts are exhausted.
- **Optional GUI**: Playable in console or with a GUI using Tkinter or PyQt.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
## Usage

**To start the console version of the game, run:**
```bash
python hangman_game.py
```

**Game Instructions:**
- A word will be chosen randomly, and you’ll see blank spaces for each letter.
- Guess letters one by one. Correct guesses reveal the letter’s position(s).
- Incorrect guesses reduce your remaining attempts.
- Guess all letters before attempts run out to win the game!

**If using the GUI version:**
```bash
python gui_version.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have ideas for improvements or bug fixes.      

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


