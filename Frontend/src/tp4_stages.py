from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4_stages import Ui_Form

class Stages (QWidget, Ui_Form):

    def __init__(self, filter_chosen, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()

        self.filter_selected = filter_chosen

        #HIDESSSSS
        self.Q_valor.hide()
        self.fo_valor.hide()
        self.DR_valor.hide()
        self.label_28.hide()
        self.label_31.hide()
        self.widget_Stages.hide()

        self.MplWidget2.show_toolbar(self.Toolbar2)
        self.plot_zp()


        #RADIO BUTTONSSS
        self.Select_button_1.toggled.connect(self.selected)
        self.Select_button_2.toggled.connect(self.superposed)
        self.Select_button_3.toggled.connect(self.total)



        #BUTTONSSS
        self.Create_button.clicked.connect(self.create_stage)




    def plot_zp(self):
        self.PyZ_Widget.canvas.ax.clear()

        self.PyZ_Widget.canvas.ax.grid()
        self.PyZ_Widget.canvas.ax.set_title("Poles and Zeros")
        self.PyZ_Widget.canvas.ax.set_xlabel("Real")
        self.PyZ_Widget.canvas.ax.set_ylabel("Imaginary")
        self.filter_selected.plot_zp(self.PyZ_Widget.canvas.ax, "red")
        self.PyZ_Widget.canvas.ax.legend(loc="best")


        self.PyZ_Widget.canvas.draw()

    def create_stage (self):
        print("create stage")

    def selected (self):
        print("selected")

    def superposed (self):
        print("superposed")

    def total (self):
        print("total")