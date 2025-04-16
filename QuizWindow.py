from tkinter import E
import requests
import html
from PyQt6.QtWidgets import QWidget,QLabel,QVBoxLayout

class QuizWindow(QWidget):
    def __init__(self,category):
        super().__init__()
        self.setWindowTitle(f"{category} Quiz")
        self.layout = QVBoxLayout(self)

        self.category = category
        self.questions = []
        self.current_question = 0 

    def load_questions(self):
        category_map = {
           "General": 9,
           "Science": 17,
           "Math": 19,
           "History": 23,
        }
        category_id = category_map.get(self.category,9)
        url = f"https://opentdb.com/api.php?amount=10&category={category_id}&type=multiple"

        try:
            response = requests.get(url)
            data = response.json()
            if data["response_code"] == 0:
                self.questions = data["results"]
                self.show_questions()
            else:
                self.layout.addWidget(QLabel("No questions found."))
        except requests.RequestException as e:
            self.layout.addWidget(QLabel(f"Error loading questions: {e}"))
            print(e)

    def show_questions(self):
        question_data = self.questions[self.current_question]
        question = html.unescape(question_data["question"])
        self.layout.addWidget(QLabel(f"Q{self.current_question_index + 1}: {question}"))