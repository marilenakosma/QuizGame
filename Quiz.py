from email.charset import QP
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt6.QtGui import QIcon,QFont,QPixmap

class LoginWindow(QWidget):
   def __init__(self):
    super().__init__()
    self.setWindowTitle("Login")
class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My first Quiz Game")
     self.setGeometry(0,0,500,500)
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

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()