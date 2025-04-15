from email.charset import QP
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFormLayout, QWidget,QLineEdit,QGridLayout,QMessageBox,QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt6.QtGui import QIcon,QFont,QPixmap

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (title and initial size)
        self.setWindowTitle("Login Form")
        self.setGeometry(0,0,300, 250)  # (x, y, width, height)

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QFormLayout to arrange the widgets
        form_layout = QFormLayout()

        # Create QLabel and QLineEdit widgets for username
        username_label = QLabel("Username:")
        self.username_field = QLineEdit()

        # Create QLabel and QLineEdit widgets for password
        password_label = QLabel("Password:")
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)


        # Create a QPushButton for login
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        # Add widgets to the form layout
        form_layout.addRow(username_label, self.username_field)
        form_layout.addRow(password_label, self.password_field)
        form_layout.addRow(login_button)

        # Set the layout for the central widget
        central_widget.setLayout(form_layout)

    def login(self):
        # Retrieve the username and password entered by the user
        username = self.username_field.text()
        password = self.password_field.text()

        # Check if the username and password are valid (for demonstration purposes)
        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Login Successful", "Welcome, " + username + "!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My first Quiz Game")
     self.setGeometry(0,0,500,500)
     self.initUI()

    def initUI(self):
     self.setWindowIcon(QIcon("Assets/Quiz.jpg"))
     self.setStyleSheet("background-color: white;")
     label=QLabel(self)
     
     pixmap = QPixmap("Assets/Quiz.jpg")
     label.setPixmap(pixmap)

     widget= QWidget()
     self.setCentralWidget(widget)

     label.setScaledContents(True);

     self.button  = QPushButton("Start Playing",self);  
     self.button.setStyleSheet("font-size:20px;" 
     "border-radius: 8px;"
     "border:1px solid;"
     "background-color: #4CAF50;" 
     "font-family:Roboto;")
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
 window = LoginWindow()
 window.show()
 app.exec()