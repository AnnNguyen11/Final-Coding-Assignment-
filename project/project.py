from flask import Flask, render_template, request, redirect, url_for, session
import random
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session

# Word lists - in a real app, these would be in separate files
def load_words(filename):
    """Reads words from a text file and returns a list."""
    try:
        with open(filename, "r") as file:
            words = [line.strip().upper() for line in file]  # Read and clean words
        return words
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

# Load words dynamically from text files
WORD_LISTS = {
    'fruits': load_words("fruits.txt"),
    'countries': load_words("countries.txt"),
    'random': load_words("random_words.txt")
}
@app.route('/')
def index():
    # Reset game state when visiting the home page
    session.clear()
    return render_template('index.html')

@app.route('/select_category/<category>')
def select_category(category):
    if category in WORD_LISTS:
        # Initialize game state
        word = random.choice(WORD_LISTS[category])
        session['word'] = word
        session['guessed_letters'] = []
        session['wrong_guesses'] = 0
        session['game_over'] = False
        session['category'] = category
        return redirect(url_for('game'))
    return redirect(url_for('index'))

@app.route('/game')
def game():
    if 'word' not in session:
        return redirect(url_for('index'))
    
    word = session['word']
    guessed_letters = session.get('guessed_letters', [])
    wrong_guesses = session.get('wrong_guesses', 0)
    game_over = session.get('game_over', False)
    category = session.get('category', '')
    
    # Create display word with guessed letters
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    
    # Check if the player has won
    won = '_' not in display_word
    
    # Check if the player has lost
    lost = wrong_guesses >= 6
    
    if won or lost:
        session['game_over'] = True
    
    # Additional debug print
    print(f"Word: {word}")
    print(f"Guessed Letters: {guessed_letters}")
    print(f"Display Word: {display_word}")
    
    return render_template(
        'game.html',
        category=category.capitalize(),
        display_word=' '.join(display_word),
        guessed_letters=', '.join(guessed_letters),
        wrong_guesses=wrong_guesses,
        game_over=session['game_over'],
        won=won,
        lost=lost,
        word=word
    )

@app.route('/guess', methods=['POST'])
def guess():
    if 'word' not in session or session['game_over']:
        return redirect(url_for('game'))
    
    letter = request.form.get('letter', '').upper()
    
    if letter and letter.isalpha() and len(letter) == 1:
        # Get current guessed letters
        guessed_letters = session.get('guessed_letters', [])
        
        # Add letter to guessed letters if not already guessed
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            session['guessed_letters'] = guessed_letters
            
            # Check if letter is in the word
            if letter not in session['word']:
                session['wrong_guesses'] = session.get('wrong_guesses', 0) + 1
    
    # Debug print
    print(f"Guessed Letter: {letter}")
    print(f"Updated Guessed Letters: {session.get('guessed_letters', [])}")
    print(f"Wrong Guesses: {session.get('wrong_guesses', 0)}")
    
    return redirect(url_for('game'))

@app.route('/new_game')
def new_game():
    if 'category' in session:
        category = session['category']
        return redirect(url_for('select_category', category=category))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)