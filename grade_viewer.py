from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from window import Ui_MainWindow

import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.assignments = []

        self.addButton.clicked.connect(self.add_grade)
        self.removeButton.clicked.connect(self.remove_grade)

        self.summary.setText("You have no assignments.")

    def add_grade(self):
        earned = self.earnedEntry.value()
        possible = self.possibleEntry.value()
        if possible:
            grade = earned / possible * 100
            self.assignments.append({"earned": earned,
                                     "possible": possible,
                                     "grade": grade,
                                     "letter": self.letter_grade(grade)})
            self.update_grades()

    def remove_grade(self):
        selections = self.gradesTable.selectedItems()
        rows_to_delete = reversed(sorted(list(set([selection.row() for selection in selections]))))
        for row in rows_to_delete:
            del self.assignments[row]
        self.update_grades()

    def update_grades(self):
        self.gradesTable.clearContents()
        self.gradesTable.setRowCount(len(self.assignments))
        if len(self.assignments) != 0:
            earned_sum, possible_sum = [], []
            for index, assignment in enumerate(self.assignments):
                self.gradesTable.setItem(index, 0, QTableWidgetItem(str(assignment["earned"])))
                self.gradesTable.setItem(index, 1, QTableWidgetItem(str(assignment["possible"])))
                self.gradesTable.setItem(index, 2, QTableWidgetItem(str(assignment["grade"]) + "%"))
                self.gradesTable.setItem(index, 3, QTableWidgetItem(assignment["letter"]))

                earned_sum.append(assignment["earned"])
                possible_sum.append(assignment["possible"])

            final_grade = round(sum(earned_sum) / sum(possible_sum) * 100, 2)
            self.summary.setText(f"""You have {len(self.assignments)} assignment{"s" if len(self.assignments) > 1 else ""}.

Your total grade: {sum(earned_sum)}/{sum(possible_sum)} ({final_grade}%) ({self.letter_grade(final_grade)})""")
        else:
            self.summary.setText("You have no assignments.")

    def letter_grade(self, grade):
        if 98 <= grade:
            return "A+"
        elif 93 <= grade <= 97:
            return "A"
        elif 90 <= grade <= 92:
            return "A-"
        elif 87 <= grade <= 89:
            return "B+"
        elif 83 <= grade <= 86:
            return "B"
        elif 80 <= grade <= 82:
            return "B-"
        elif 77 <= grade <= 79:
            return "C+"
        elif 73 <= grade <= 76:
            return "C"
        elif 70 <= grade <= 72:
            return "C-"
        elif 67 <= grade <= 69:
            return "D+"
        elif 63 <= grade <= 66:
            return "D"
        elif 60 <= grade <= 62:
            return "D-"
        elif grade <= 59:
            return "F"


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Grade Viewer")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
