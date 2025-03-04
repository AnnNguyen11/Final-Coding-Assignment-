import unittest
from flask import session
from project import app  # Ensure the main Flask app file is named project.py

class HangmanTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test_secret_key'
        self.client = app.test_client()

    def test_homepage(self):
        """Test if the homepage loads and resets the session."""
        with self.client as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertFalse('word' in session)
            self.assertFalse('guessed_letters' in session)

    def test_select_category(self):
        """Test if selecting a category initializes the game state."""
        with self.client as client:
            response = client.get('/select_category/fruits', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('word', session)
            self.assertIn('guessed_letters', session)
            self.assertIn('wrong_guesses', session)
            self.assertEqual(session['wrong_guesses'], 0)

    def test_valid_guess(self):
        """Test that a correct letter guess is processed correctly."""
        with self.client as client:
            client.get('/select_category/fruits', follow_redirects=True)
            session['word'] = 'APPLE'  # Mock a known word
            response = client.post('/guess', data={'letter': 'A'}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('A', session['guessed_letters'])
            self.assertEqual(session['wrong_guesses'], 0)  # No wrong guess

    def test_invalid_guess(self):
        """Test that an incorrect letter guess increments the wrong guess count."""
        with self.client as client:
            client.get('/select_category/fruits', follow_redirects=True)
            session['word'] = 'APPLE'  # Mock a known word
            response = client.post('/guess', data={'letter': 'Z'}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Z', session['guessed_letters'])
            self.assertEqual(session['wrong_guesses'], 1)  # Wrong guess should be counted

    def test_game_over(self):
        """Test that the game ends after 6 wrong guesses."""
        with self.client as client:
            client.get('/select_category/fruits', follow_redirects=True)
            session['word'] = 'APPLE'  # Mock a known word
            for i in range(6):
                client.post('/guess', data={'letter': chr(65 + i)}, follow_redirects=True)  # A, B, C, D, E, F
            self.assertTrue(session['game_over'])
            
if __name__ == '__main__':
    unittest.main()
