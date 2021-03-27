from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/message_input', methods = ['GET', 'POST'])
def message_input():
    if request.method == 'POST':
        user = request.form['message']
        return render_template('message_input.html', user = user)
    else:
        user = request.args.get('message')
        return render_template('message_input.html', user = user)
    
@app.route('/view')
def view():
    return render_template('view.html')



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')