#creaate simple flask app
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from openaiapi import chat


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chat', methods=["GET",'POST'])
def chet():
    while True:
        user = request.form['input']
        assistant = chat(user)
        return render_template('index.html', assistant=assistant, user=user)
    

if __name__ == '__main__':
    app.run(debug=True)