import random
from PyQt6.QtGui import QIcon
import requests
import html
from PyQt6.QtWidgets import QMessageBox, QProgressBar, QWidget,QLabel,QVBoxLayout,QPushButton
from PyQt6.QtCore import Qt,QDir
from PyQt6.QtGui import QIcon,QFont,QPixmap,QFontDatabase
from db import save_score

class QuizWindow(QWidget):
    def __init__(self, category, username, difficulty):
        super().__init__()
        self.category = category
        self.username = username
        self.difficulty = difficulty
        self.current_question = 0
        self.score = 0
        self.questions = []

        self.setWindowTitle("Quiz Game")
        self.setGeometry(0, 0, 800, 600)
        self.setStyleSheet("background-color: #F4F6FC;")
        QFontDatabase.addApplicationFont("Assets/static/Roboto-Light.ttf")
        QFontDatabase.addApplicationFont("Assets/static/Montserrat-Medium.ttf")
        self.setWindowIcon(QIcon("Assets/Quiz.jpg"))

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(10)
        self.progress_bar.setValue(0)
        
        self.progress_bar.setStyleSheet("""
    QProgressBar {
        border: 2px solid #292D53;
        border-radius: 10px;
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        font-size: 14px;
        color: #fff;
        background-color: #365880;  /* Dark purple bg */
    }

    QProgressBar::chunk {
        background-color: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #00FFFF, stop:1 #FF00FF
        );
        border-radius: 10px;
        margin: 1px;
    }
""")
        self.progress_bar.setFixedHeight(25)
        self.layout.addWidget(self.progress_bar)

    # Score label
        self.score_label = QLabel("Score: 0")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_label.setStyleSheet("""
                                       QLabel {
                                           font-family: 'Montserrat', sans-serif;
                                           font-size: 20px;
                                           font-weight: bold;
                                           color: #292D53; 
                                           padding:15px; 
                                           background-color: #EAF1FF;
                                           border: 2px solid transparent;
                                           border-radius: 10px;
                                           }
                                           """)
        self.score_label.setContentsMargins(0,0,0,0)
        self.score_label.setFixedWidth(150)
        self.score_label.setFixedHeight(30)
        self.layout.addWidget(self.score_label)

    # Question layout (only this gets cleared)
        self.question_layout = QVBoxLayout()
        self.layout.addLayout(self.question_layout)

        self.load_questions()

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
      
     for i in reversed(range(self.question_layout.count())):
       while self.question_layout.count():
         item = self.question_layout.takeAt(0)
         widget = item.widget()
         if widget is not None:
           widget.deleteLater()


     question_data = self.questions[self.current_question]
     question = html.unescape(question_data["question"])

     correct = html.unescape(question_data["correct_answer"]) #html.unescape() turns weird codes like &amp; or &#039; into real characters.
     incorrect = [html.unescape(ans) for ans in question_data["incorrect_answers"]]
     options = incorrect + [correct]
     random.shuffle(options)
     

     label = QLabel(question)
     label.setWordWrap(True)
     label.setAlignment(Qt.AlignmentFlag.AlignCenter)
     label.setStyleSheet("""
                QLabel {
                    font-family:'Montserrat',sans-serif;
                    font-size:18px;
                    border: 2px solid #292D53;
                    border-radius: 10px;
                    text-align: center;
                    font-family: 'Montserrat', sans-serif;
                    color: #292D53;
                    background-color:#EAF1FF;
                    background-clip:padding-box;
                    border-image:linear-gradient(to right,#00FFF,#FF00FF) 1;
                }
            """)
     self.question_layout.addWidget(label)
     
     for option in options:
        btn = QPushButton(option)
        btn.clicked.connect(lambda _,ans=option: self.check_answer(ans,correct))
        btn.setStyleSheet("""
                QPushButton {
                    font-family: 'Montserrat', sans-serif;
                    border: 2px solid transparent;
                    border-radius: 10px;
                    text-align: center;
                    font-size: 16px;
                    color: black;
                    background-color: white;
                    
                }
                QPushButton:hover {
                 background-color: qlineargradient(
                  spread:pad, x1:0, y1:0, x2:1, y2:0,
                  stop:0 #00FFFF, stop:1 #FF00FF
        );
                    border: 2px solid #3E8EED;
                }
            """)
        self.question_layout.addWidget(btn)


    def check_answer(self,selected,correct):
        if selected == correct:
           self.score += 1
        else:
           pass
        
        self.current_question += 1
        self.progress_bar.setValue(self.current_question)
        self.score_label.setText(f"Score: {self.score}")
        self.show_question()
    
    def score_screen_button_style(self):
      return """
        QPushButton {
            font-family: 'Montserrat', sans-serif;
            background-color: #3EB2FD;;
            color: black;
            border: 2px solid white;
            border-radius: 15px;
            padding: 10px 20px;
            font-size: 18px;
        }
        QPushButton:hover {
            background-color: #5EC6FF;
            border: 2px solid #FF00FF;
            color: white;
        }
    """
    
    def restart_quiz(self):
      self.clear_layout(self.layout)
        
      self.current_question = 0
      self.score = 0
      self.progress_bar.setValue(0)
      self.score_label.setText("Score: 0")
      
      self.layout.addWidget(self.progress_bar)
      self.layout.addWidget(self.score_label)
      self.layout.addLayout(self.question_layout)

    # Reload questions
      self.load_questions()
      
    def clear_layout(self, layout):
     while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().setParent(None)

      
    def end_quiz(self):
     save_score(self.username, self.score, self.category)
     
     self.clear_layout(self.question_layout)
             
     title = QLabel("Quiz Complete!")
     title.setAlignment(Qt.AlignmentFlag.AlignCenter)
     title.setStyleSheet("""
                        QLabel {
                            font-family:'Montserrat',sans-serif;
                            font-size:32px;
                            color:#3EB2FD;
                            font-weight:bold;
                        }
                        """)
     self.layout.addWidget(title)
     
     retry_btn = QPushButton("Play Again")
     retry_btn.clicked.connect(self.restart_quiz)
     retry_btn.setStyleSheet(self.score_screen_button_style())
     self.layout.addWidget(retry_btn)

    # Exit Button
     exit_btn = QPushButton("Exit")
     exit_btn.clicked.connect(self.close)
     exit_btn.setStyleSheet(self.score_screen_button_style())
     self.layout.addWidget(exit_btn)
    
    

