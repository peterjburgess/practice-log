from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-log', methods=['POST', 'GET'])
def create_log():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('create-log.html')
