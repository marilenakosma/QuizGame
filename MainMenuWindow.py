from email.charset import QP
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QComboBox, QWidget,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon,QFontDatabase
from QuizWindow import QuizWindow

class MainMenuWindow(QWidget):
    def __init__(self,username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Select Quiz Category")
        self.setFixedSize(800,500)  
        self.setStyleSheet("background-color: #F4F6FC;")
        QFontDatabase.addApplicationFont("Assets/static/Roboto-Light.ttf")
        QFontDatabase.addApplicationFont("Assets/static/Montserrat-Medium.ttf")
        self.setWindowIcon(QIcon("Assets/Quiz.jpg"))

        layout = QVBoxLayout()
        #layout.setSpacing(10)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
       
        header = QLabel(f"Welcome, {self.username}!")
        header.setStyleSheet("font-size: 30px; font-weight: bold; margin-bottom: 15px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        difficulty = QLabel("First,select a difficulty:")
        difficulty.setStyleSheet("font-family:Montserrat; font-size: 16px; margin-bottom: 15px;")
        difficulty.setAlignment(Qt.AlignmentFlag.AlignCenter)

        category_header = QLabel("Then,select a quiz category to start playing.")
        category_header.setStyleSheet("font-family:Montserrat; font-size: 16px; margin-bottom: 15px;")
        layout.addWidget(header)
    

        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Easy", "Medium", "Hard"])


        card_layout = QHBoxLayout()
        card_layout.setSpacing(20)
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icons = {
            "General":"Assets/general.png",
             "Science":"Assets/science.png",
             "Math":"Assets/math.jpg",
             "History":"Assets/history.png",
        }
        categories = ["General", "Science", "Math", "History"]
        for i, name in enumerate(categories):
            btn = QPushButton(name)
            btn.setFixedSize(180,180)

            if name in icons:
              btn.setIcon(QIcon(icons[name]))
              btn.setIconSize(QSize(100, 100))

            btn.clicked.connect(lambda _, cat=name: self.open_quiz(cat))
            btn.setStyleSheet("""
                QPushButton {
                    font-family: 'Roboto', sans-serif;
                    background-color: white;
                    border-radius: 15px;
                    border: 2px solid #E0E0E0;
                    font-size: 16px;
                    text-align:center;
                }
                QPushButton:hover {
                    background-color: #EAF1FF;
                    border: 2px solid #3E8EED;
                }
            """)
            card_layout.addWidget(btn)
            #grid.addWidget(btn, i // 2, i % 2)

        self.difficulty_combo.setStyleSheet("""
            QComboBox {
                 font-size: 14px;
                 padding: 6px;
                 border: 1px solid #ccc;
                 border-radius: 6px;
                 background-color: white;
            }
            QComboBox:hover {
                border: 1px solid #3E8EED;
            }
        """)
        #layout.addLayout(grid)
        spacer = QSpacerItem(0,20,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Fixed)

        layout.addWidget(difficulty, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.difficulty_combo, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addItem(spacer)
        layout.addWidget(category_header, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addItem(spacer)
        layout.addLayout(card_layout)
        self.setLayout(layout)
        
    def open_quiz(self, category):
     difficulty = self.difficulty_combo.currentText().lower()
     self.quiz_window = QuizWindow(category,self.username,difficulty,self)
     self.quiz_window.show()
     self.close()