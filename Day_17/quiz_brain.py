class QuizBrain:
    def __init__(self, question_list: list, question_number: int = 0, question_score: int = 0):
        self.question_number = question_number
        self.question_list = question_list
        self.question_score = question_score

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(
            f"Q{self.question_number + 1}: {current_question.text} (True/False) ?:\n")
        self.question_number += 1

        self.check_is_answer_correct(user_answer, current_question.answer)

    def check_is_next_question(self):
        return self.question_number < len(self.question_list)

    def check_is_answer_correct(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"Your answer is correct !")
            self.question_score += 1
            return True
        else:
            print(f"Your answer is incorrect !")
        print(f"The correct answer is {correct_answer}")
        print(
            f"Your current score is {self.question_score}/{self.question_number}")
