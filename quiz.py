import json
import os

def load_questions(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return None
    
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data.get('questions', [])
    except json.JSONDecodeError:
        print(f"Error: The JSON file is incorrectly formatted.")
        return None

def display_question(question_data):
    print(question_data['question'])
    for idx, choice in enumerate(question_data['choices']):
        print(f"{idx + 1}. {choice}")

def get_user_answer():
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= 4:
                return answer - 1
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    questions = load_questions('questions.json')
    if questions is None:
        return
    
    score = 0

    for question_data in questions:
        display_question(question_data)
        user_answer = get_user_answer()
    
        if user_answer == question_data['correct_index']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['choices'][question_data['correct_index']]}\n")
    
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()