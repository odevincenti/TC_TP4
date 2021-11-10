from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4_stages import Ui_Form
from Frontend.src.Stage_Widget import StageWidget

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
        self.set_ZP()


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

    def set_ZP(self):
        self.Poles_Box.addItems(self.filter_selected.get_pole_pairs())
        self.Zeros_box.addItems(self.filter_selected.get_zero_pairs())


    def create_stage (self):
        print("create stage")
        self.aux_stage = StageWidget()
        #self.Stages_Widget.layout().addWidget(self.aux_curve)

    def selected (self):
        print("selected")
        self.show_graph()

    def superposed (self):
        print("superposed")
        self.show_graph()

    def total (self):
        print("total")
        self.show_graph()

    # def add_stage_widget(self):
    #     numerador = self.numerador_teorico.text()
    #     denominador = self.denominador_teorico.text()
    #     num_coef = numerador.split(',')
    #     den_coef = denominador.split(',')
    #
    #     num_len = len(num_coef)
    #     num_str = ""
    #     for i in range(0, num_len):
    #         if (num_len - i) > 2:
    #             num_str += str(num_coef[i]) + ".s^" + str(num_len - 1 - i) + "+"
    #         elif (num_len - i) == 2:
    #             num_str += str(num_coef[i]) + ".s +"
    #         else:
    #             num_str += str(num_coef[i])
    #
    #     den_len = len(den_coef)
    #     den_str = ""
    #     for i in range(0, den_len):
    #         if (den_len - i) > 2:
    #             den_str += str(den_coef[i]) + ".s^" + str(den_len - 1 - i) + "+"
    #         elif (den_len - i) == 2:
    #             den_str += str(den_coef[i]) + ".s +"
    #         else:
    #             den_str += str(den_coef[i])
    #     self.label_numerador.setText(num_str)
    #     self.label_denominador.setText(den_str)


    def show_graph(self):
        print("show graph")