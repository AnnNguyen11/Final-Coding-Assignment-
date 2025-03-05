Team: NAY AND ANN
Project: Hangman game...
Project: HANGMAN
Video Demo: https://youtube.com/shorts/OKoU0wQaeC8?feature=share 
Description: Hangman, random word generator, fun 

hangman.py: The main Python script containing the Flask application.
templates: Directory containing HTML templates.
index.html: The home page for selecting a category.
game.html : The game page for guessing letters.
fruits.txt countries.txt, random_words.txt: Text files containing word lists for each category.

 Code Explanation

The core logic of the game is implemented in the hangman.py script. Here's a breakdown of the main components:

Flask Routes:
Renders the home page and clears the session.
select_category, category, Selects a random word from the chosen category and initializes the game state.
game: Displays the game board and handles win/loss conditions.
guess: Processes letter guesses and updates the game state.
new_game: Restarts the game with the same category.

Sessions Flask sessions are used to store and manage the game state, including the hidden word, guessed letters, and wrong guesses.
Word Loading: The load_words function reads words from text files, and the WORD_LISTS dictionary stores the word lists for each category.
Game Logic: The game logic involves generating the display word, checking for win/loss conditions, and updating the game state based on user input.
