from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Grade Viewer")

    window = MainWindow()
    app.exec_()
