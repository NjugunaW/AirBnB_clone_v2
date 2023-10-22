#!/usr/bin/python3
"""A script that starts a Flask web application
Web application listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable 
    /python/(<text>): display “Python ”, followed by the value of the text
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
    /number_odd_or_even/<n>: display a HTML page only if n is an integer
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer
    """
    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run('0.0.0.0')
