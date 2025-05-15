from PyQt6.QtCore import Qt


def button_styling(button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #3EB2FD;
                background-image: linear-gradient(1deg, #4F58FD, #149BF3 99%);
                border-radius: 100px;
                border-width: 0;
                color: white;
                border: none;
                padding: 10px;
                font-weight: bold;
                border-radius: 5px;
                font-size: 14px;
                margin-top: 10px;
            }
            QPushButton:hover {
            background-color: #5EC6FF;
            border: 2px solid #FF00FF;
            color: white;
        }
        """)
        button.setCursor(Qt.CursorShape.PointingHandCursor)