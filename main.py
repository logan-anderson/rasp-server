from flask import Flask, render_template
import threading
import time
from gpiozero import LED
app = Flask(__name__)
green = LED(3)
red = LED(2)
yellow = LED(4)

stop_threads = False


def help_function(delay=.3):
    all_off()
    while True:
        green.on()
        time.sleep(delay)
        green.off()
        red.on()
        time.sleep(delay)
        red.off()

        global stop_threads
        if stop_threads:
            break


t_help = threading.Thread(target=help_function)


def start_t_help():
    global t_help
    t_help = threading.Thread(target=help_function)
    t_help.start()


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
    def setup_func():
        all_off()
        global stop_threads
        global t_help
        if t_help.is_alive():
            stop_threads = True
            t_help.join()

    if color == 'green':
        setup_func()
        green.on()
    if color == 'yellow':
        setup_func()
        yellow.on()
    if color == 'red':
        setup_func()
        red.on()
    if color == 'help':
        start_t_help()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
