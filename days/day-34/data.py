import html
import requests
from question_model import Question

def load_questions() -> list[dict]:
    parameters = {
        "amount": 10,
        "type": "boolean"

    }
    response = requests.get('https://opentdb.com/api.php', params=parameters)
    response.raise_for_status()
    questions_json = response.json()
    return questions_json['results']


def load_question_bank() -> list[Question]:
    question_bank = []
    for question in load_questions():
        question_text = html.unescape(question["question"])
        question_answer = bool(question["correct_answer"])
        question_category = html.unescape(question['category'])
        new_question = Question(question_text, question_answer, question_category)
        question_bank.append(new_question)
    return question_bank