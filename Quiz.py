from email.charset import QP
import sys
from PyQt6.QtCore import Qt,QDir
from PyQt6.QtWidgets import QFormLayout, QWidget,QLineEdit,QGridLayout,QMessageBox,QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt6.QtGui import QIcon,QFont,QPixmap,QFontDatabase

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

        self.login_button = QPushButton("Login")
        button_styling(self.login_button)

        layout.addWidget(self.title)
        layout.addWidget(self.username_field)
        layout.addWidget(self.password_field)
        layout.addWidget(self.login_button)


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

if __name__=='__main__':
 app = QApplication(sys.argv)
 window = MainWindow()
 window.show()
 app.exec()