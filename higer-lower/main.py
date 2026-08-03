from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def hello_world():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400 style="display: block; margin: auto;">'

n = randint(0,9)
@app.route('/<int:number>')
def check(number):
    if number > n:
        return '<h1 style="color: red; text-align: center">Too high, try again</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400 style="display: block; margin: auto;">'
    elif number < n:
        return '<h1 style="color: purple; text-align: center">Too low, try again</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400 style="display: block; margin: auto;">'
    else:
        return '<h1 style="color: green; text-align: center">You found me!</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400 style="display: block; margin: auto;">'




if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)