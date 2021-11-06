from Frontend.src.menu import MainWindowQ
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':


    app = QApplication([])

    window = MainWindowQ()
    window.show()

    app.exec()


