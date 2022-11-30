from flask import Flask

app = Flask(__name__)


def convert_celsius_to_fahrenheit(celsius):
    """Convert from celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello{name}"


@app.route('/f')
@app.route('/f/<celsius>')
def show_celsius_to_fahrenheit_conversion(celsius=0):
    """Display celsius to fahrenheit conversion calculation"""
    return f"<h1>{float(celsius)}C is {convert_celsius_to_fahrenheit(float(celsius))}F<h1>"


if __name__ == '__main__':
    app.run()
