import data

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer



class QuestionImporter:
    def __init__(self):
        pass

    @staticmethod
    def import_questions_from_db():
        questions = []
        for q in data.question_data:
            questions.append(Question(q['text'], q['answer']))
        return questions

    @staticmethod
    def import_questions_from_open_trivia():
        questions = []
        for q in data.data_from_db["results"]:
            questions.append(Question(q['question'], q['correct_answer']))
        return questions