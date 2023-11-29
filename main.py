import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit
from gui import GradeCalculatorApp

def run_gui():
    app = QApplication(sys.argv)
    window = GradeCalculatorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_gui()
