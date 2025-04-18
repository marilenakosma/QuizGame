from email.charset import QP
import sys
from PyQt6.QtCore import QSize, Qt,QDir
from PyQt6.QtWidgets import QComboBox, QFormLayout, QWidget,QLineEdit,QGridLayout,QMessageBox,QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon,QFont,QPixmap,QFontDatabase
from db import save_user,authenticate_user
from urllib.request import urlopen
import json
import pandas as pd
import random
import html
from QuizWindow import QuizWindow


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
        """)
        button.setCursor(Qt.CursorShape.PointingHandCursor)