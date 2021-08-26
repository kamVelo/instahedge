from flask import Flask, render_template,redirect,request, session, url_for
file = open("login.txt", "r")
username = file.readline()
password = file.readline()
file.close()

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def home():
    return render_template('index.html')