import sys
from PyQt6.QtWidgets import QApplication
from MainMenuWindow import MainMenuWindow  
from MainWindow import MainWindow  # Entry point from MainMenuWindow
from QuizWindow import QuizWindow  # Entry point from MainMenuWindow
from LoginWindow import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #main_menu = MainMenuWindow(username="marilena")
    #window = QuizWindow(category="math",username="marilena",difficulty="easy", main_menu=main_menu)
    window = MainWindow()
    window.show()  # Show main menu window
    sys.exit(app.exec())  # Start the app
