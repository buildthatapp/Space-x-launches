from flask import Flask, render_template, url_for, get_flashed_messages

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

app.run(host='127.0.0.1', debug=True, port='5000')