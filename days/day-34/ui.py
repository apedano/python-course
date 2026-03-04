from tkinter import *
from question_model import Question

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, answer_true_callback, answer_false_callback):
        self.__answer_true_callback=answer_true_callback
        self.__answer_false_callback=answer_false_callback
        self.__window = Tk()
        self.__window.title("Quiz Game")
        self.__window.config(bg=THEME_COLOR, padx=20, pady=20, width=600, height=600)

        self.__label_status = Label(self.__window, text="I am a label", font=("Courier", 10, "bold"))
        self.__label_status.grid(row=0, column=1)



        self.__canvas_category = Canvas(width=300, height=20)
        self.__category_text_id = self.__canvas_category.create_text(150, 10, text="Question category",
                                                              width=250,
                                                              font=("Arial", 10, "bold"))
        self.__canvas_category.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.__canvas_question = Canvas(width=300, height=250)
        self.__question_text_id = self.__canvas_question.create_text(170, 100, text="Question goes HERE but it is very long",
                                                              width=250,
                                                              font=("Arial", 15, "italic"))
        self.__canvas_question.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        # Creating a photoimage object to use image
        self.__photo_true = PhotoImage(file=r"images/true.png")
        self.__true_button = Button(self.__window, text='', image=self.__photo_true, command=self.__answer_true_callback)
        self.__true_button.grid(row=3, column=0, padx=20, pady=20)
        self.__photo_false = PhotoImage(file=r"images/false.png")
        self.__false_button = Button(self.__window, text='', image=self.__photo_false, command=self.__answer_false_callback)
        self.__false_button.grid(row=3, column=1, padx=20, pady=20)


    def show_correct_answer(self, score: int, question_number:int) -> None:
        self.show_answer(score, question_number, "GREEN")

    def show_wrong_answer(self, score: int, question_number:int) -> None:
        self.show_answer(score, question_number, "RED")

    def show_answer(self, score: int, question_number:int, color:str) -> None:
        self.__canvas_question.config(bg=color)
        self.__label_status.config(text=f"Score: {score} / {question_number}")
        # Force redraw (usually not even necessary)
        self.__window.update_idletasks()

    def run(self):
        self.__window.mainloop()


    def set_question(self, question: Question) -> None:
        self.__canvas_category.itemconfig(self.__category_text_id, text=question.category)
        self.__canvas_question.itemconfig(self.__question_text_id, text=question.text)
        self.__canvas_question.config(bg="WHITE")


    def finish_quiz(self) -> None:
        self.__canvas_category.itemconfig(self.__category_text_id, text="Quiz finished")
        self.__canvas_question.itemconfig(self.__question_text_id, text="You can read the score above!")
        self.__true_button.destroy()
        self.__false_button.destroy()



