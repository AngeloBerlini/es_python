from flask import Flask, render_template
import json


#1
def read_recipes(recipe: str) -> None:
    with open("esercizio_40.json", "r") as f:
        recipe = json.load(f)
    print(recipe)

#2
def get_recipe_by_id(recipe_id: int) -> None:
    with open("esercizio_40.json", "r") as f:
        recipe = json.load(f)
    for recipe in recipe:
        if recipe["id"] == recipe_id:
            print(recipe)
            return recipe
    print(f"Nessuna flashcard trovata per l'ID {recipe_id}")


#3
def prompt_for_id() -> int:
    recipe_id = int(input("Inserisci l'ID della flashcard "))
    return recipe_id

#4
app = Flask(__name__)

@app.route('/recipe/<int:id>')
def recipe(id):
    recipe = get_recipe_by_id(id)
    return render_template('recipe.html', recipe=recipe)