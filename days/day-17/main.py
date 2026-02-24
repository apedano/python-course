from question_model import Question, QuestionImporter


class QuizGame:

    def __init__(self):
        self.questions = QuestionImporter().import_questions_from_open_trivia()

    def play_quiz(self):
        score = 0
        question_number = 1
        for question in self.questions:
            if self._ask_question(question, question_number):
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
            print(f"Your score is {score}/{len(self.questions)}")
            question_number += 1
        print("The game is over")


    def _ask_question(self, question: Question, question_number: int):
        print(f"Q.{question_number} : {question.text}")
        user_answer = ""
        while user_answer not in ["True", "False"]:
            if user_answer != "":
                print("Please enter either True or False.")
            user_answer=input("true or false?:").title()
        return user_answer == question.answer


QuizGame().play_quiz()
