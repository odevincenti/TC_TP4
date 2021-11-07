from PyQt5.QtWidgets import QWidget, QVBoxLayout
from Frontend.src.ui.tp4 import Ui_Form
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

#se crea una widget con 1 layout
#adentro hay un canvas con una figura
class MplWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)  #agrego el canvas

        self.canvas.ax = self.canvas.figure.add_subplot(111)
        self.setLayout(self.layout)
        #self.canvas.draw()

    def show_toolbar(self, layout):
        layout.addWidget(NavigationToolbar(self.canvas, self))