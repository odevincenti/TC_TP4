from PyQt5.QtWidgets import QWidget, QVBoxLayout
from Frontend.src.ui.tp4 import Ui_Form
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


#se crea una widget con 1 layout
#adentro hay un canvas con una figura
class Matplotlib(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.canvas)  #agrego el canvas
        self.canvas.draw()