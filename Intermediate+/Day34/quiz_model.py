import html


class Quiz:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = {}

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, given_answer):
        right_answer = self.current_question.answer
        if given_answer.lower() == right_answer.lower():
            self.score += 1
            return True
        else:
            return False
