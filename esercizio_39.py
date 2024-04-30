from flask import Flask, render_template
import json




app = Flask(__name__)



@app.route('/flashcard/<id>')   
def display_form(id:int):
    with open("esercizio_39.json", "r") as f:
        
    flashcard={
        "id": 2,
        "question":"What is the capital of Spain?",
        "answer": "Ratas"
    }
    return render_template('esercizio_39.html', flashcard=flashcard)

if __name__ == '__main__':
    app.run(debug=True, port=3537)