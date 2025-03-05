project: HANGMAN
Video Demo: https://youtube.com/shorts/OKoU0wQaeC8?feature=share 
Description: Hangman, random word generator, fun 

# Hangman Web Game

This is a simple, interactive web-based version of the well-known Hangman game developed with the Flask web framework in Python. It enables users to play Hangman interactively in their web browser, guessing letters to reveal a secret word. This project is ideal for beginners and those interested in learning the fundamentals of web development with Python and Flask.

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Setup and Installation](#setup-and-installation)
* [How to Play](#how-to-play)
* [File Structure](#file-structure)
* [Code Explanation](#code-explanation)
* [Detailed Functionality and Design Choices](#detailed-functionality-and-design-choices)


## Project Overview

This is a simple yet fun Hangman game, created as a working example of a dynamic web application using Python and the Flask microframework. It shows how easy it is to build a full-featured dynamic web application without needing to delve into the minutiae of creating a full framework. Flask session usage makes up the basic concept behind game design, where one can maintain game states related to a user to give a consistent and unbroken game experience without losing progress. The project is intentionally designed moddable to enable users to attempt to tinker and add functionality to it.

## Features

* *Multiple Word Categories:* Offers a selection of word categories (fruits, countries, random) to enhance replay value and provide varied challenges.
* *Persistent Session-Based Game State:* Utilizes Flask sessions to store and preserve game state securely, offering a continuous and seamless user experience.
* *Dynamic Word Loading from Files:* Word lists are loaded from external text files, allowing easy addition, modification, or expansion of the game content.
* *Simple-to-Use Game Interface:* Shows the mystery word, letters that have been guessed, and incorrect guesses in a clear and brief, easy-to-understand format.
* *Solid Win/Loss Logic:* Calculates correct game outcomes from user guesses, with intuitive feedback.
* *Inconvenience-Free New Game Button:* Offers a way for users to simply start a new game with the same category, for convenient replay.
* *Basic Error Handling:* Contains file existence checks to prevent application crashes due to missing word lists and to offer a more consistent experience.
* *Simple and Understandable Codebase:* The codebase is built to be easy and simple to comprehend, ensuring it is an ideal reference point for learning web development concepts.

## Technologies Used

* *Python:* The underlying programming language, providing the application with its basic logic and functionality.
* *Flask:* A lightweight and flexible web framework, used to develop the web application and handle HTTP requests.
* *HTML:* Used to structure the web pages, defining the user interface and the layout of the game.
* *CSS (Optional):* Can be used to make the visual presentation and styling of the game more appealing.
* *os Module:* Used to generate secure secret keys for session management, making the application more secure.

## Setup and Installation

1.  *Clone the Repository (Optional):* Clone the repository to your local system if you are using Git so that you can easily update and use the code.
2.  *Create Word Files:* Create three-word files, fruits.txt, countries.txt, and random_words.txt, within the project directory. Add a single word per line to each file.
3.  *Install Flask:* In your command prompt or terminal, enter pip install Flask. This will install the Flask web framework.
4.  *Run the Application:* Navigate to the project directory and enter python hangman.py. This will execute the Flask development server.
5.  *Access the Game:* Navigate to a web browser and enter http://127.0.0.1:5000/. The game should be accessible.
6.  *Create HTML files:* Create a folder called templates in the same directory as the Python file. Inside that folder create index.html and game.html.

## How to Play

1.  *Category Selection:* On the home page, select a category to begin the game.
2.  *Guessing Letters:* Enter a letter in the input field and click "Guess" to submit your guess.
3.  *Progress Tracking:* Monitor the hidden words, guessed letters, and bad guesses to monitor your progress.
4.  *Game Outcome:* Keep guessing until you correctly guess the word or have used up all attempts.
5.  *New Game:* Press "New Game" to play a new game with the same theme.

## File Structure

## Code Explanation

The bulk of the Hangman game functionality is in hangman.py. The most important parts are:

* *Flask Routes:* Define the application's URL routing and handle user requests.
* *Session Management:* Store and restore individual user game state.
* *Word List Handling:* Read word lists from files external to the application.
* *Game Logic:* Implement the rules for Hangman, such as winning and losing.

## Detailed Functionality and Design Decisions

* **/ Route:** The index route begins the game by clearing the session and showing the category selection page. This creates a clean start for each new game.
* **/select_category/<category> Route:** This route selects a random word from the specified category and initializes the game state in the session. This allows more categories to be added with ease.
* **/game Route:** Displays the game page, including the game state and hidden word. It also has win/loss condition logic.
* **/guess Route:** Handles user letter guesses, updates the game state, and checks for win/loss conditions. Sessions are used to save the game state between requests.
* **/new_game Route:** Resets the game with the same category, with an instant replay.
* *Word Loading:* The load_words function loads words from text files, and WORD_LISTS holds these lists. This modular approach allows easy addition or modification of word lists.
* *Session Management:* Flask sessions are used to hold and keep track of the game state, i.e., the secret word, guessed characters, and wrong guesses. This keeps the game state consistent throughout the user's session.


