from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat
import sqlite3
from flask_apscheduler import APScheduler

sense = SenseHat()

app = Flask(__name__)


scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reminder')
def reminder():
    return render_template('/reminder.html')






if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')