class QuizBrain:
    def __init__(self, question_list: list, question_number: int = 0):
        self.question_number = question_number 
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q{self.question_number + 1}: {current_question.text} (True/False) ?:\n")
        self.question_number += 1
        
    def check_is_next_question(self):
        if self.question_number >= len(self.question_list):
            return True
        else : 
            return False 