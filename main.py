import sys
from PyQt6.QtWidgets import QApplication
from MainMenuWindow import MainMenuWindow  
from MainWindow import MainWindow  # Entry point from MainMenuWindow
#from QuizWindow import QuizWindow  # Entry point from MainMenuWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainMenuWindow(username="marilena")
    #window = QuizWindow(category="math",username="marilena",difficulty="easy")
    #window = MainWindow()
    window.show()  # Show main menu window
    sys.exit(app.exec())  # Start the app
