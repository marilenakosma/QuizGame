from email.charset import QP
import sys
from PyQt6.QtCore import Qt,QDir
from PyQt6.QtWidgets import QFormLayout, QWidget,QLineEdit,QGridLayout,QMessageBox,QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt6.QtGui import QIcon,QFont,QPixmap,QFontDatabase
from db import save_user,authenticate_user
from urllib.request import urlopen
import json
import pandas as pd
import random
import html
from QuizWindow import QuizWindow

with urlopen("https://opentdb.com/api.php?amount=50&category=14&difficulty=medium&type=multiple") as webpage:
   data = json.loads(webpage.read().decode())
   df= pd.DataFrame(data['results'])
   print(df.head())

def preload_data():
   question = df["question"][0]
   correct=df["correct_answer"][0]
   wrong = df["incorrect_answers"][0]

   parameters["question"].append(question)
   parameters["question"].append(correct)
   all_answers= wrong + [correct]
   random.shuffle(all_answers)
   parameters["answer1"].append(all_answers[0])
   parameters["answer2"].append(all_answers[1])
   parameters["answer3"].append(all_answers[2])
   parameters["answer4"].append(all_answers[3])
   print(all_answers)

parameters={"question: []",
            "answer1: []",
            "answer2: []",
            "answer3: []",
            "answer4: []",
            "correct:[]"}

preload_data
def button_styling(button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #3EB2FD;
                background-image: linear-gradient(1deg, #4F58FD, #149BF3 99%);
                border-radius: 100px;
                border-width: 0;
                color: white;
                border: none;
                padding: 10px;
                font-weight: bold;
                border-radius: 5px;
                font-size: 14px;
                margin-top: 10px;
            }
        """)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My first Quiz Game")
     self.setGeometry(0,0,500,500)
     self.initUI()

    def initUI(self):
     self.setWindowIcon(QIcon("Assets/quiz.jpg"))
     self.setStyleSheet("background-color: white;" 
                        "border: 1px solid #ccc;"
                        "border-radius:10px;")
     label=QLabel(self)
     
     pixmap = QPixmap("Assets/Quiz.jpg")
     label.setPixmap(pixmap)

     widget= QWidget()
     self.setCentralWidget(widget)

     label.setScaledContents(True);

     self.button  = QPushButton("Start Playing",self);  
     button_styling(self.button)
     self.button.clicked.connect(self.on_click)
     
     layout = QVBoxLayout()
     
     layout.addWidget(label,alignment=Qt.AlignmentFlag.AlignCenter)
     layout.addWidget(self.button,alignment=Qt.AlignmentFlag.AlignAbsolute)
        
     widget.setLayout(layout)
     self.setCentralWidget(widget)

    def on_click(self):
       self.w = LoginWindow()
       self.w.show()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(500,500)  # Optional: fixed size
        self.setWindowIcon(QIcon("Assets/Quiz.jpg"))

        layout = QVBoxLayout()
        QFontDatabase.addApplicationFont("Assets/static/Roboto-Light.ttf")
        QFontDatabase.addApplicationFont("Assets/static/Montserrat-Medium.ttf")

        self.title = QLabel("Welcome")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px;")

        self.username_field = QLineEdit()
        self.username_field.setPlaceholderText("Username")

        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Password")
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)
       
        btn_layout = QHBoxLayout()

        self.login_button = QPushButton("Login")
        button_styling(self.login_button)
        
        self.register_button = QPushButton("Register")
        button_styling(self.register_button)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

        layout.addWidget(self.title)
        layout.addWidget(self.username_field)
        layout.addWidget(self.password_field)
        btn_layout.addWidget(self.login_button)
        btn_layout.addWidget(self.register_button)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                           font-size:15px;
                           background-color:#f2f2f2;
                           }
            QLineEdit { 
                           background-color:white;
                           font-family: 'Roboto', sans-serif;
                           border: 1px solid #ccc;
                           border-radius:5px;
                           font-size:14px;
            }
                           """)
        
    def login(self):
           username = self.username_field.text()
           password = self.password_field.text()     
           if authenticate_user(username,password):
              QMessageBox.information(self, "Login Successful", f"Welcome, {username}!")
              self.open_main_window(username)
           else:
              QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def register(self):
           username = self.username_field.text()
           password = self.password_field.text()     
           if save_user(username,password):
              QMessageBox.information(self, "Successful Registration", f"Welcome, {username}!")
           else:
              QMessageBox.warning(self, "Error", "Username already exists.")
    
    def open_main_window(self,username):
        self.main = MainMenuWindow(username)
        self.main.show()
        self.close()
class MainMenuWindow(QWidget):
    def __init__(self,username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Select Quiz Category")
        self.setStyleSheet("background-color: #F4F6FC;")
        QFontDatabase.addApplicationFont("Assets/static/Roboto-Light.ttf")
        self.setWindowIcon(QIcon("Assets/Quiz.jpg"))

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
       
        header = QLabel(f"Welcome, {self.username}!")
        header.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        grid = QGridLayout()
        grid.setSpacing(15)

        categories = ["General", "Science", "Math", "History"]
        for i, name in enumerate(categories):
            btn = QPushButton(name)
            btn.setFixedSize(200,200)
            btn.clicked.connect(lambda checked,category=name:self.open_quiz(category))
            btn.setStyleSheet("""
                QPushButton {
                    font-family: 'Roboto', sans-serif;
                    background-color: white;
                    border-radius: 15px;
                    border: 2px solid #E0E0E0;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #EAF1FF;
                    border: 2px solid #3E8EED;
                }
            """)
            grid.addWidget(btn, i // 2, i % 2)

        layout.addLayout(grid)

        # 🔹 Navigation Buttons (optional)
        nav_layout = QHBoxLayout()
        prev_btn = QPushButton("◀ Prev")
        next_btn = QPushButton("Next ▶")
        for btn in (prev_btn, next_btn):
            btn.setStyleSheet("padding: 8px; font-size: 14px;")
            
        nav_layout.addWidget(prev_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(next_btn)
        layout.addLayout(nav_layout)

        # 🔹 Bottom Start/Select Button
        select_btn = QPushButton("Start Quiz")
        select_btn.setStyleSheet("""
            QPushButton {
                background-color: #3E8EED;
                color: white;
                padding: 12px;
                border-radius: 20px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #256FD1;
            }
        """)
        layout.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def open_quiz(self, category):
     self.quiz_window = QuizWindow(category)
     self.quiz_window.show()
     self.close()

if __name__=='__main__':
 app = QApplication(sys.argv)
 window = LoginWindow()
 window.show()
 app.exec()