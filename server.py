"""
********************************************************************************
* Project Name:  Flask Number Guessing Game
* Description:   This project is a simple number guessing game built using Flask. The goal is for the user to guess a random number between 0 and 9. The app provides feedback on whether the guess is too high, too low, or correct. It uses dynamic responses and fun GIFs to enhance the user experience.
* Author:        ziqkimi308
* Created:       2025-01-04
* Updated:       2025-01-04
* Version:       1.0
********************************************************************************
"""

from flask import Flask
import random

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
	return "<h1>Guess a number between 0 and 9</h1>" \
			"<img src='https://media.giphy.com/media/1BFFVB9WvJNUnBIYVy/giphy.gif' width='400'>"

random_numb = random.randint(0, 9)

@flask_app.route("/<int:guess>")
def guess_number(guess):
	if guess > random_numb:
		return "<h1 style='color:red'>Too high, try again!</h1>" \
				"<img src='https://media.giphy.com/media/WYnLED53FGVXQ2IHGr/giphy.gif' width='600'>"
	elif guess < random_numb:
		return "<h1 style='color:blue'>Too low, try again!</h1>" \
				"<img src='https://media.giphy.com/media/ORSdGwpofi2tDx9pTS/giphy.gif' width='400'>"
	elif guess == random_numb:
			return "<h1 style='color:green'>Correcttttt!</h1>" \
			"<img src='https://media.giphy.com/media/FnF7vgz2oON3i/giphy.gif' width='400'>"

if __name__ == "__main__":
	flask_app.run(debug=True)