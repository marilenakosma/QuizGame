import random
import requests
import html
from PyQt6.QtWidgets import QMessageBox, QWidget,QLabel,QVBoxLayout,QPushButton
from PyQt6.QtCore import Qt,QDir
from db import save_score

class QuizWindow(QWidget):
    def __init__(self,category,username):
        super().__init__()
        self.username = username
        self.setWindowTitle(f"{category} Quiz")
        self.setFixedSize(800, 600)  # or whatever size you want
        self.layout = QVBoxLayout()  # ✅ right
        self.setLayout(self.layout)
        
        self.category = category
        self.questions = []
        self.current_question = 0
        self.score = 0  
        self.load_questions()

    def load_questions(self):
        print("[DEBUG] load_questions() called!")  # 👈 Add this
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
            print(data) 
            if data["response_code"] == 0:
             self.questions = data["results"]
             self.show_question()
            else:
             self.layout.addWidget(QLabel("No questions found."))
        except Exception as e:
          print("API Error:", e)
          self.layout.addWidget(QLabel("Failed to load questions."))

    def show_question(self):
     if self.current_question >= len(self.questions):
        self.end_quiz()
        return
      
     for i in reversed(range(self.layout.count())):
        widget = self.layout.itemAt(i).widget()
        if widget:
           widget.setParent(None)

     question_data = self.questions[self.current_question]
     question = html.unescape(question_data["question"])

     correct = html.unescape(question_data["correct_answer"]) #html.unescape() turns weird codes like &amp; or &#039; into real characters.
     incorrect = [html.unescape(ans) for ans in question_data["incorrect_answers"]]
     options = incorrect + [correct]
     random.shuffle(options)

     label = QLabel(question)
     label.setWordWrap(True)
     label.setAlignment(Qt.AlignmentFlag.AlignCenter)
     label.setStyleSheet("font-size: 18px; margin: 20px;")
     self.layout.addWidget(label)

     for option in options:
        btn = QPushButton(option)
        btn.clicked.connect(lambda _,ans=option: self.check_answer(ans,correct))
        self.layout.addWidget(btn)

    def check_answer(self,selected,correct):
        if selected == correct:
           print("Correct!")
        else:
           print("Incorrect!")

        self.current_question += 1
        self.show_question()

    def end_quiz(self):
     save_score(self.username, self.score, self.category)
     result = QMessageBox.question(
        self, "Quiz Finished", f"You scored {self.score}/{len(self.questions)}.\nTry again?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
     
     if result == QMessageBox.StandardButton.Yes:
        self.current_question = 0
        self.score = 0
        self.show_question()
     else:
        self.close()  # Or go back to main menu, etc.
