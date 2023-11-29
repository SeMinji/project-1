from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit
from logic import calculate_statistics, calculate_grade

class GradeCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Grade Calculator")
        self.setGeometry(100, 100, 400, 300)

        self.num_students_label = QLabel("Total number of students:")
        self.num_students_entry = QTextEdit()

        self.scores_label = QLabel("Enter scores separated by space:")
        self.scores_entry = QTextEdit()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_grades)

        self.output_label = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.num_students_label)
        layout.addWidget(self.num_students_entry)
        layout.addWidget(self.scores_label)
        layout.addWidget(self.scores_entry)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def calculate_grades(self):
        try:
            num_students = int(self.num_students_entry.toPlainText())
            scores = list(map(int, self.scores_entry.toPlainText().split()))

            if num_students <= 0 or any(score < 0 for score in scores):
                raise ValueError("Invalid input. Please enter positive numbers and scores.")

            best_score, average_score = calculate_statistics(scores)

            output_text = ""
            for i, score in enumerate(scores):
                grade = calculate_grade(score, best_score)
                output_text += f"Student {i + 1} score is {score} and grade is {grade}\n"

            grade_for_average = calculate_grade(average_score, best_score)
            output_text += f"\nThe average score is {average_score:.2f}, a grade of {grade_for_average}"

            self.output_label.setPlainText(output_text)

        except ValueError as e:
            self.output_label.setPlainText(str(e))
