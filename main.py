from flask import Flask, render_template
from gpiozero import LED
app = Flask(__name__)
green = LED(3)
red = LED(2)
yellow = LED(4)


def all_off():
    yellow.off()
    green.off()
    red.off()


all_off()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/on/<color>')
def update_color(color):
    all_off()
    if color == 'green':
        green.on()
    if color == 'yellow':
        yellow.off()
    if color == 'red':
        red.off()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
