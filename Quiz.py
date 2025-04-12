import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt6.QtGui import QIcon,QFont,QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My first Quiz Game")
     self.setGeometry(0,0,500,500)
     self.setWindowIcon(QIcon("Assets/Quiz.jpg"))

     label=QLabel(self)
     label.setGeometry(0,0,200,200);
     
     pixmap = QPixmap("Assets/Quiz.jpg")
     label.setPixmap(pixmap)
     
     label.setScaledContents(True);
     label.setGeometry((self.width() - label.width() )// 2,
                       (self.height() - label.height() )//2,
                       label.width(),label.height())
"""
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    
     label = QLabel("Hello",self)
     label.setFont(QFont("Arial",40))
     label.setGeometry(0,0,500,100)

     label.setStyleSheet("color:blue;" 
     "background-color:#6fdcf7;" 
     "font-weight:bold;" )

     label.setAlignment(Qt.AlignmentFlag.AlignHCenter) #Vertical Alignment
"""

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()