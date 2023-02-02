from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_imgage = PhotoImage(file="Day_34/images/true.png")
        false_image = PhotoImage(file="Day_34/images/false.png")

        self.true_button = Button(image=true_imgage, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions() : 
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.ask_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else: 
            self.canvas.itemconfig(self.question_text, text="End of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.inform_user(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        self.inform_user(self.quiz.check_answer("False"))
        
    def inform_user(self, is_correct :bool):
        if is_correct : 
            self.canvas.config(bg="green")
        else : 
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        