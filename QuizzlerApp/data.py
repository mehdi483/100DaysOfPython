import requests

TRIVIA_API_ADDRESS = "https://opentdb.com/api.php"
TRIVIA_API_PARAMS = {"amount": 10, "type": "boolean"}


def get_questions():
    questions = requests.get(url=TRIVIA_API_ADDRESS, params=TRIVIA_API_PARAMS)
    questions.raise_for_status()
    return questions.json()["results"]


question_data = get_questions()
