from PyQt6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)
window = QWidget()
window.show()
sys.exit(app.exec())

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__(self)
        