from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4_stages import Ui_Form
from Frontend.src.Stage_Widget import StageWidget

class Stages (QWidget, Ui_Form):

    def __init__(self, filter_chosen, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()

        self.filter_selected = filter_chosen

        self.stage_array = []


        #HIDESSSSS
        self.Q_valor.hide()
        self.fo_valor.hide()
        self.label_28.hide()
        self.widget_Stages.hide()

        self.MplWidget2.show_toolbar(self.Toolbar2)
        self.plot_zp()
        self.set_ZP()


        #RADIO BUTTONSSS
        self.Select_button_1.toggled.connect(self.selected)
        self.Select_button_2.toggled.connect(self.superposed)
        self.Select_button_3.toggled.connect(self.total)



        #BUTTONSSS
        self.Create_button.clicked.connect(self.create_stage)
        self.delete_stage_button.clicked.connect(self.delete_stage)


    def plot_zp(self):
        self.PyZ_Widget.canvas.ax.clear()

        self.PyZ_Widget.canvas.ax.grid()
        self.PyZ_Widget.canvas.ax.set_title("Poles and Zeros")
        self.filter_selected.plot_zp(self.PyZ_Widget.canvas.ax, "red")
        self.PyZ_Widget.figure.tight_layout()
        self.PyZ_Widget.canvas.draw()

    def set_ZP(self):
        self.Poles_Box.addItems(self.filter_selected.get_pole_pairs())
        self.Zeros_box.addItems(self.filter_selected.get_zero_pairs())


    def create_stage (self):
        print("create stage")
        self.aux_stage = StageWidget()
        self.stage_array.append(self.aux_stage)
        self.Stages_Widget.layout().addWidget(self.aux_stage)

    def delete_stage(self):
        print("delete stage")

    def selected (self):
        print("selected")
        self.show_graph()

    def superposed (self):
        print("superposed")
        self.show_graph()

    def total (self):
        print("total")
        self.show_graph()


    def show_graph(self):
        print("show graph")