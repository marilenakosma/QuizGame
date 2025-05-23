from PyQt6.QtCore import  Qt
from PyQt6.QtWidgets import QWidget,QMainWindow,QLabel,QPushButton,QVBoxLayout
from PyQt6.QtGui import QIcon,QPixmap
from LoginWindow import LoginWindow
from button_styling import button_styling

class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My first Quiz Game")
     self.setFixedSize(500,500)
     self.initUI()

    def initUI(self):
     self.setWindowIcon(QIcon("Assets/quiz.jpg"))
     self.setStyleSheet("background-color: white;")
     label=QLabel(self)
     
     pixmap = QPixmap("Assets/quiz.jpg")
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
       self.close()
