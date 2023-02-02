import requests
import html


PARAMS = {
    "amount": 10,
    "type": "boolean"
}


class QuizBrain:

    def __init__(self):
        self.request = requests.get(
            url="https://opentdb.com/api.php", params=PARAMS)
        self.request.raise_for_status()
        self.data = self.request.json()
        self.results = self.data['results']

        self.current_question_number = 0
        self.current_question = None
        self.current_answer = None

        self.score = 0

    def get_question(self):
        if self.current_question_number < 10:
            self.current_question = self.results[self.current_question_number]['question']
            self.current_answer = self.results[self.current_question_number]['correct_answer']
            self.current_question_number += 1
        else:
            self.current_question_number = 0

    def still_has_questions(self):
        if self.current_question_number < len(self.results):
            return True

    def ask_question(self):
        self.get_question()
        question_text = html.unescape(self.current_question)
        return f"Q.{self.current_question_number}: {question_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_answer
        if user_answer.upper() == correct_answer.upper():
            self.score += 1
            return True
        else:
            return False 
