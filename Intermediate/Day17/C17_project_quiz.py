from data import question_data
from question_model import Question
from quiz_model import Quiz

questions = []

for data_set in question_data:
    question_text = data_set['question']
    question_answer = data_set['correct_answer']
    questions.append(Question(question_text, question_answer))

quiz = Quiz(questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quiz.score} / {quiz.question_number}.")