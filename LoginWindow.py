from email.charset import QP
import sys
from PyQt6.QtCore import QSize, Qt,QDir
from PyQt6.QtWidgets import QComboBox, QFormLayout, QWidget,QLineEdit,QGridLayout,QMessageBox,QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon,QFont,QPixmap,QFontDatabase
from db import save_user,authenticate_user
from button_styling import button_styling
from MainMenuWindow import MainMenuWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(400,400)
        self.setWindowIcon(QIcon("Assets/Quiz.jpg"))
        self.initUI()

    def initUI(self):
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
                           background-color:#EAF1FF;
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