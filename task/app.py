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

@app.route('/reminder', methods = ['GET', 'POST'])
def reminder():
    if request.method == 'POST':
        reminder = request.form['reminder']
        setdate = request.form['setdate']
        
        display = reminder + setdate

        #connecting to database
        conn = sqlite3.connect('./static/data/tasks.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO reminders(reminder, setdate) VALUES ((?), (?))", (reminder, setdate))
        conn.commit()
        #close database connection
        conn.close()

        sense.show_message(display)

        return render_template('/reminder.html', reminder = reminder, setdate = setdate)
    
    else:
         reminder = request.args.get('reminder')
         setdate = request.args.get('setdate')
    return render_template('/reminder.html', reminder = reminder, setdate = setdate)

@app.route('/completed')
def completed():
    return render_template('/completed.html')

@app.route('/deleted')
def deleted():
    return render_template('/delete.html')

@app.route('/edit')
def edit():
    return render_template('/edit.html')





if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')