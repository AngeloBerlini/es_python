from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')

   
def display_links():
    with open('pithon/esercizio37.json') as f:
        data = json.load(f)
    return render_template('esercizio37.html', text=data)


if __name__ == '__main__':
    app.run(debug=True, port=3536)