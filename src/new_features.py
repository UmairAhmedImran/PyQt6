#using classes to make a simple application

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()