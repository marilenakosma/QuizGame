import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel


class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setGeometry(700,300,500,500)
     self.button = QPushButton("Click me!",self)
     self.label = QLabel("Hello",self)
     self.initUI()

    def initUI(self):
       self.button.setGeometry(150,200,200,100)
       self.button.setStyleSheet("font-size:30px;")
       self.button.clicked.connect(self.on_click) #You need a signal(clicked) that connects to an slot(self.on_click)
       #The signal is an event and the slot is the action

       self.label.setGeometry(150,300,200,100)
       self.label.setStyleSheet("font-size:50px")

    def on_click(self):
     self.label.setText("Goodbye")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()