from flask import Flask, render_template, url_for, request
from flaskext.mysql import MySQL
import datetime
import pymysql.cursors

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Nanakojo@1'
app.config['MYSQL_DATABASE_DB'] = 'dictionary'

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_response = ''
    if request.method == 'POST':
        user_input = request.form['word'] 
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('select meaning from word where word = %s', (user_input,))
        rv = cur.fetchall()
        if(len(rv) > 0):
            user_response = rv[0]['meaning']
        else:
            user_response = 'The word cannot be found in this dictionary, please try again with another word'
    return render_template('index.html', user_response=user_response)

@app.route('/dashboard')
def dashboard(): 
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)