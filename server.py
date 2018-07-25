from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
    get_all_friends_query = "SELECT * FROM friends"
    all_friends = mysql.query_db(get_all_friends_query)
    return render_template('index.html', friends = all_friends)

@app.route('/add_friends', methods=["post"])
def add_friend():
    add_friend_query = "INSERT INTO friends (name, age, friend_since) VALUES (:name, :age, :friend_since)"
    data = { 'name': request.form['name'],
             'age': request.form['age'],
             'friend_since': request.form['friend']}
    mysql.query_db(add_friend_query, data)
    return redirect('/')

app.run(debug=True)
