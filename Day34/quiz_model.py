import html

class Quiz:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(answer, current_question.answer)
        return answer

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, given_answer, correct_answer):
        if given_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer} ")
        print(f"Your current score: {self.score} / {self.question_number}")
        print('\n')
