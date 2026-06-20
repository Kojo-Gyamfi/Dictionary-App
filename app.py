from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/dashboard')
def about():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)