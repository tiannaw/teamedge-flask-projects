from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat
import sqlite3

sense = SenseHat()


app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/message_input', methods = ['GET', 'POST'])
def message_input():
    if request.method == 'POST':
        user = request.form['message']
        name = request.form['name']

        display = name + user

        #connect to database and insert message and name 
        conn = sqlite3.connect('./static/data/messages.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO message(name, message) VALUES ((?), (?))", (name, user))
        conn.commit()
        #close database connection
        conn.close()

        sense.show_message(display) 

        return render_template('message_input.html', user = user, name = name)
   
    else:
         user = request.args.get('message')
         name = request.args.get('name')
         return render_template('message_input.html', user = user, name = name)
    
@app.route('/view', methods = ['GET', 'POST'])
def view():
    #connecting to database 
    conn = sqlite3.connect('./static/data/messages.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name': row[0], 'message': row[1]}
        messages.append(message)
    conn.close()
    return render_template('view.html', messages = messages)



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')