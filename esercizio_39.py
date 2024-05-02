from flask import Flask, render_template
import json

# Step 1: Read and print the JSON data
def read_flashcards(filename: str) -> None:
    with open(filename, "r") as f:
        flashcards = json.load(f)
    print(flashcards)


# Step 2: Access individual flashcards
def get_flashcard_by_id(flashcard_id: int, filename: str) -> None:
    with open(filename, "r") as f:
        flashcards = json.load(f)
    for flashcard in flashcards:
        if flashcard["id"] == flashcard_id:
            print(flashcard)
            return flashcard
    print(f"Nessuna flashcard trovata per l'ID {flashcard_id}")


# Step 3: Create a simple CLI interface
def prompt_for_id() -> int:
    flashcard_id = int(input("Inserisci l'ID della flashcard "))
    return flashcard_id

# Step 4: Allow the user to answer a question
def prompt_for_answer() -> str:
    user_answer = input("Inserisci la risposta: ")
    return user_answer


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.lower() == correct_answer.lower()



if __name__ == '__main__':
    #Test delle funzioni
    filename = "esercizio_39.json"  
    read_flashcards(filename)
    flashcard_id = prompt_for_id()
    flashcard = get_flashcard_by_id(flashcard_id, filename)
    if flashcard:
        user_answer = prompt_for_answer()
        is_correct = check_answer(user_answer, flashcard['answer'])
        if is_correct:
            print("Correct!")
        else:
            print("Incorrect. The correct answer was: " + flashcard['answer'])



app = Flask(__name__)



@app.route('/')   
def display_form():
    return render_template('esercizio_39.html')


@app.route('/flashcards', methods=["POST"])   
def display_success():
        