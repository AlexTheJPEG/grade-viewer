# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradesBox = QtWidgets.QGroupBox(self.centralwidget)
        self.gradesBox.setGeometry(QtCore.QRect(10, 10, 481, 441))
        self.gradesBox.setObjectName("gradesBox")
        self.gradesTable = QtWidgets.QTableWidget(self.gradesBox)
        self.gradesTable.setGeometry(QtCore.QRect(10, 20, 461, 281))
        self.gradesTable.setObjectName("gradesTable")
        self.gradesTable.setColumnCount(4)
        self.gradesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gradesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gradesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gradesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gradesTable.setHorizontalHeaderItem(3, item)
        self.summary = QtWidgets.QTextBrowser(self.gradesBox)
        self.summary.setGeometry(QtCore.QRect(10, 310, 461, 55))
        self.summary.setObjectName("summary")
        self.addButton = QtWidgets.QPushButton(self.gradesBox)
        self.addButton.setGeometry(QtCore.QRect(10, 370, 151, 31))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.gradesBox)
        self.removeButton.setGeometry(QtCore.QRect(165, 370, 141, 31))
        self.removeButton.setObjectName("removeButton")
        self.earnedEntry = QtWidgets.QDoubleSpinBox(self.gradesBox)
        self.earnedEntry.setGeometry(QtCore.QRect(379, 376, 91, 21))
        self.earnedEntry.setObjectName("earnedEntry")
        self.possibleEntry = QtWidgets.QDoubleSpinBox(self.gradesBox)
        self.possibleEntry.setGeometry(QtCore.QRect(379, 406, 91, 21))
        self.possibleEntry.setObjectName("possibleEntry")
        self.earnedLabel = QtWidgets.QLabel(self.gradesBox)
        self.earnedLabel.setGeometry(QtCore.QRect(330, 380, 47, 13))
        self.earnedLabel.setObjectName("earnedLabel")
        self.possibleLabel = QtWidgets.QLabel(self.gradesBox)
        self.possibleLabel.setGeometry(QtCore.QRect(330, 410, 47, 13))
        self.possibleLabel.setObjectName("possibleLabel")
        self.mockTestBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mockTestBox.setGeometry(QtCore.QRect(500, 10, 501, 441))
        self.mockTestBox.setObjectName("mockTestBox")
        self.testButton = QtWidgets.QPushButton(self.mockTestBox)
        self.testButton.setGeometry(QtCore.QRect(20, 140, 141, 23))
        self.testButton.setObjectName("testButton")
        self.possibleEntryMock = QtWidgets.QDoubleSpinBox(self.mockTestBox)
        self.possibleEntryMock.setGeometry(QtCore.QRect(70, 30, 91, 21))
        self.possibleEntryMock.setObjectName("possibleEntryMock")
        self.mockTestResults = QtWidgets.QTextBrowser(self.mockTestBox)
        self.mockTestResults.setGeometry(QtCore.QRect(181, 15, 311, 416))
        self.mockTestResults.setObjectName("mockTestResults")
        self.possibleLabelMock = QtWidgets.QLabel(self.mockTestBox)
        self.possibleLabelMock.setGeometry(QtCore.QRect(20, 33, 47, 13))
        self.possibleLabelMock.setObjectName("possibleLabelMock")
        self.maxLetterSelection = QtWidgets.QComboBox(self.mockTestBox)
        self.maxLetterSelection.setGeometry(QtCore.QRect(85, 70, 76, 22))
        self.maxLetterSelection.setObjectName("maxLetterSelection")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterSelection.addItem("")
        self.maxLetterLabel = QtWidgets.QLabel(self.mockTestBox)
        self.maxLetterLabel.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.maxLetterLabel.setObjectName("maxLetterLabel")
        self.showAllResultsCheck = QtWidgets.QCheckBox(self.mockTestBox)
        self.showAllResultsCheck.setGeometry(QtCore.QRect(20, 110, 101, 17))
        self.showAllResultsCheck.setObjectName("showAllResultsCheck")
        self.extraAssignmentsLabel = QtWidgets.QLabel(self.mockTestBox)
        self.extraAssignmentsLabel.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.extraAssignmentsLabel.setObjectName("extraAssignmentsLabel")
        self.possibleEntryMock2 = QtWidgets.QDoubleSpinBox(self.mockTestBox)
        self.possibleEntryMock2.setGeometry(QtCore.QRect(20, 240, 91, 21))
        self.possibleEntryMock2.setObjectName("possibleEntryMock2")
        self.possibleEntryMock3 = QtWidgets.QDoubleSpinBox(self.mockTestBox)
        self.possibleEntryMock3.setGeometry(QtCore.QRect(20, 270, 91, 21))
        self.possibleEntryMock3.setObjectName("possibleEntryMock3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gradesBox.setTitle(_translate("MainWindow", "Grades"))
        item = self.gradesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Earned"))
        item = self.gradesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Possible"))
        item = self.gradesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Grade"))
        item = self.gradesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Letter"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.earnedLabel.setText(_translate("MainWindow", "Earned:"))
        self.possibleLabel.setText(_translate("MainWindow", "Possible:"))
        self.mockTestBox.setTitle(_translate("MainWindow", "Mock Test"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.possibleLabelMock.setText(_translate("MainWindow", "Possible:"))
        self.maxLetterSelection.setItemText(0, _translate("MainWindow", "A+"))
        self.maxLetterSelection.setItemText(1, _translate("MainWindow", "A"))
        self.maxLetterSelection.setItemText(2, _translate("MainWindow", "A-"))
        self.maxLetterSelection.setItemText(3, _translate("MainWindow", "B+"))
        self.maxLetterSelection.setItemText(4, _translate("MainWindow", "B"))
        self.maxLetterSelection.setItemText(5, _translate("MainWindow", "B-"))
        self.maxLetterSelection.setItemText(6, _translate("MainWindow", "C+"))
        self.maxLetterSelection.setItemText(7, _translate("MainWindow", "C"))
        self.maxLetterSelection.setItemText(8, _translate("MainWindow", "C-"))
        self.maxLetterSelection.setItemText(9, _translate("MainWindow", "D+"))
        self.maxLetterSelection.setItemText(10, _translate("MainWindow", "D"))
        self.maxLetterSelection.setItemText(11, _translate("MainWindow", "D-"))
        self.maxLetterSelection.setItemText(12, _translate("MainWindow", "F"))
        self.maxLetterLabel.setText(_translate("MainWindow", "Max letter:"))
        self.showAllResultsCheck.setText(_translate("MainWindow", "Show all results?"))
        self.extraAssignmentsLabel.setText(_translate("MainWindow", "Extra assignments:"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionNew.setText(_translate("MainWindow", "New..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
