#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(f'{param}')
    return f'{param}'

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(param)) + "\n"
    return f"{numbers}"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1/num2}'
    elif operation == '%':
        return f'{num1 % num2}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
