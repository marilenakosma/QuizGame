import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setGeometry(700,300,500,500)
     self.line_edit = QLineEdit(self)
     self.button = QPushButton("Submit",self)
     
     self.initUI()

    def initUI(self):
      self.line_edit.setGeometry(10,10,200,40)
      self.button.setGeometry(210,10,100,40)
      self.line_edit.setStyleSheet("font-size:25px;" 
      "font-family:Arial;")
      self.button.setStyleSheet("font-size:25px;" 
      "font-family:Arial;")

      self.line_edit.setPlaceholderText("Enter your name")
      
      self.button.clicked.connect(self.submit)

    def submit(self):
      text = self.line_edit.text()
      print(f"Hello {text}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()