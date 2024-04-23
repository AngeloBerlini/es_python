from flask import Flask, render_template,request
import json

app = Flask(__name__)

@app.route('/')   
def display_form():
    return render_template('esercizio_38.html')

@app.route('/success', methods=["POST"])   
def display_success():
    username = request.form['username']
    email = request.form['email']
    return render_template('success.html',uname = username,electronicmail = email)