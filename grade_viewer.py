from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from window import Ui_MainWindow

import sys
import math
import re
import decimal

grade_letters = {
    range(98, 101): "A+",
    range(93, 98):  "A",
    range(90, 93):  "A-",
    range(87, 90):  "B+",
    range(83, 87):  "B",
    range(80, 83):  "B-",
    range(77, 80):  "C+",
    range(73, 77):  "C",
    range(70, 73):  "C-",
    range(67, 70):  "D+",
    range(63, 67):  "D",
    range(60, 63):  "D-",
    range(0,  60):  "F"
}

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.assignments = []

        self.addButton.clicked.connect(self.add_grade)
        self.removeButton.clicked.connect(self.remove_grade)
        self.testButton.clicked.connect(self.mock_test)

        self.summary.setText("You have no assignments.")

        self.grade_regex = r"Your\ total\ grade: (\d+\.\d+)/(\d+\.\d+)"

    def add_grade(self):
        earned = round(self.earnedEntry.value(), 2)
        possible = round(self.possibleEntry.value(), 2)
        if possible:
            grade = round(earned / possible * 100, 2)
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

            earned_sum = round(sum(earned_sum), 2)
            possible_sum = round(sum(possible_sum), 2)
            final_grade = round((earned_sum / possible_sum) * 100, 2)

            self.summary.setText(f"""You have {len(self.assignments)} assignment{"s" if len(self.assignments) > 1 else ""}.

Your total grade: {earned_sum}/{possible_sum} ({final_grade}%) ({self.letter_grade(final_grade)})""")
        else:
            self.summary.setText("You have no assignments.")

    def mock_test(self):
        possible = self.possibleEntryMock.value()
        max_letter = self.maxLetterSelection.currentText()
        max_letter_index = list(grade_letters.values()).index(max_letter)
        show_all = self.showAllResultsCheck.isChecked()

        matches = re.findall(self.grade_regex, self.summary.toPlainText())
        if len(matches) == 0 or possible == 0:
            return
        total_earned, total_possible = (float(n) for n in matches[0])
        results_string = f"Your total grade: {total_earned}/{total_possible}\n"

        # TODO: Implement verbose results
        if not show_all:
            # TODO: Add precision options
            for earned in list(float_range(0, possible, 0.01)):
                earned = round(float(earned), 2)
                new_grade = round((earned + total_earned) / (possible + total_possible) * 100, 2)
                new_letter = self.letter_grade(new_grade)
                new_letter_index = list(grade_letters.values()).index(new_letter)

                if new_letter_index <= max_letter_index:
                    needed_grade = round(earned / possible * 100, 2)
                    needed_letter = self.letter_grade(needed_grade)
                    results_string += f"\nYou need at least a {earned}/{possible} ({needed_grade}%) ({needed_letter}):"
                    results_string += f"\n{earned + total_earned}/{possible + total_possible} ({new_grade}%) ({new_letter})"
                    break
            else:
                results_string += f"\nYou cannot get a{'n' if new_letter[0] in ('A', 'F') else ''} {max_letter}."
                results_string += f"\nMaximum score with a {possible}/{possible} (100%) (A+):"
                results_string += f"\n{possible + total_earned}/{possible + total_possible} ({new_grade}%) ({new_letter})"

            self.mockTestResults.setText(results_string)


    def letter_grade(self, grade):
        for r, g in grade_letters.items():
            if math.floor(grade) in r:
                return g


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Grade Viewer")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
