from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4_stages import Ui_Form

class Stages (QWidget, Ui_Form):

    def __init__(self, filter_chosen, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()

        #HIDESSSSS
        self.Q_valor.hide()
        self.fo_valor.hide()
        self.DR_valor.hide()
        self.label_28.hide()
        self.label_31.hide()

        self.MplWidget2.show_toolbar(self.Toolbar2)








    def plot_zp2(self):
        ax.scatter(self.zeros.real, self.zeros.imag, marker='o', edgecolors="blue", facecolors="None")
        ax.scatter(self.poles.real, self.poles.imag, marker='x', color="red", label=self.name)
        return

    def plot_zp3(self):
        self.MplWidget.canvas.ax.clear()

        self.PyZ_Widget.canvas.ax.grid()
        self.PyZ_Widget.canvas.ax.legend(loc="best")
        self.PyZ_Widget.canvas.ax.set_title("Poles and Zeros")
        self.PyZ_Widget.canvas.ax.set_xlabel("Real")
        self.PyZ_Widget.canvas.ax.set_ylabel("Imaginary")

        self.MplWidget.canvas.draw()