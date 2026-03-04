import time

from ui import *

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.__quiz_interface = QuizInterface(self.check_answer_true, self.check_answer_false)

    def start(self):
        self.next_question()
        self.__quiz_interface.run()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.__quiz_interface.set_question(self.current_question)
        # user_answer = input(f"Q.{self.question_number} ({self.current_question.category}): {self.current_question.text} (True/False): ")
        #self.check_answer(user_answer)

    def check_answer_false(self):
        self.check_answer(False)

    def check_answer_true(self):
        self.check_answer(True)

    def check_answer(self, user_answer: bool):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            self.__quiz_interface.show_correct_answer(self.score, self.question_number)
        else:
            self.__quiz_interface.show_wrong_answer(self.score, self.question_number)
        time.sleep(1)
        if self.still_has_questions():
            self.next_question()
        else:
            print("The quiz finished")
            self.__quiz_interface.finish_quiz()

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
