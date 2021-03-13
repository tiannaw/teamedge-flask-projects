from flask import Flask, render_template, current_app as current_app
import requests
from sense_hat import SenseHat

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def about():
    return  render_template('index.html')

@app.route('/message_input', methods = ['GET', 'POST'])
def message_input():
    if request.method == 'POST':
        user = request.form['fname']
        return render_template('message.html', name = user)
    else:
        user = request.args.get('fname')
        return render_template('message.html', name = user)



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')