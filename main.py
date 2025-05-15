import sys
from PyQt6.QtWidgets import QApplication
from MainMenuWindow import MainMenuWindow  
from MainWindow import MainWindow  
from QuizWindow import QuizWindow  
from LoginWindow import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #main_menu = MainMenuWindow(username="marilena")
    #window = QuizWindow(category="math",username="marilena",difficulty="easy", main_menu=main_menu)
    window = MainWindow()
    window.show()  
    sys.exit(app.exec())  
