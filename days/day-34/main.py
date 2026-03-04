from data import load_question_bank
from quiz_brain import QuizBrain
from ui import QuizInterface


quiz = QuizBrain(load_question_bank())

quiz.start()






# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
