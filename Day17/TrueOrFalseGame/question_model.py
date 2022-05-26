from mimetypes import init
from msilib.schema import Class

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

