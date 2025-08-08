from flask import Flask, render_template, request, redirect
# from flask_restful import Api
# from resources.user import User  # Uncomment if you have this resource
from db import get_connection

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')   

@app.route('/services',methods=['GET'])
def services():
    return render_template('services.html') 

@app.route('/technology',methods=['GET'])
def technology():
    return render_template('technology.html')

@app.route('/contactform',methods=['GET'])
def contactform():
    return render_template('contactform.html')


@app.route('/submit_user', methods=['POST'])
def submit_user():
    name = request.form.get('name')
    email = request.form.get('email')
    if not name or not email:
        return "<h3>Name and email are required!</h3><a href='/'>Go back</a>"

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
    finally:
        conn.close()

    return f"<h3>User {name} added successfully!</h3><a href='/'>Go back</a> | <a href='/all_users'>View Users</a>"

@app.route('/all_users')
def all_users():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
    finally:
        conn.close()
    # Render a simple HTML table
    html = "<h2>All Users</h2><table border='1'><tr><th>ID</th><th>Name</th><th>Email</th></tr>"
    for user in users:
        html += f"<tr><td>{user['id']}</td><td>{user['name']}</td><td>{user['email']}</td></tr>"
    html += "</table><br><a href='/'>Add another user</a>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
