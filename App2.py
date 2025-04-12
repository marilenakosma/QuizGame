import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QCheckBox
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setGeometry(700,300,500,500)
     self.checkbox=QCheckBox("Do you like food?", self) #parent widget
     self.initUI()

    def initUI(self):
     self.checkbox.setGeometry(10,0,500,100)
     self.checkbox.setStyleSheet("font-size:30px;" 
                                 "font-family:Arial;")
     self.checkbox.setChecked(False)
     self.checkbox.stateChanged.connect(self.checkbox_changed)

#PYQT6 change -when you first click the checkbox,the signal is emitted before the visual change is complete,
#so sometimes the state you receive isn't correct,stateChanged passes and integer representing the new state
    def checkbox_changed(self, state):
        if state == Qt.CheckState.Checked.value:
            print("You like food")
        else:
            print("You don't like food")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()