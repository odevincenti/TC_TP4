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
        self.aux_stage = StageWidget()
        self.aux_stage.label_2.setText("Stage " + str(len(self.stage_array) + 1))
        if self.Zeros_box.currentIndex() == -1:
            self.filter_selected.add_stage([], self.filter_selected.pole_pairs[self.Poles_Box.currentIndex()])
        else:
            self.filter_selected.add_stage(self.filter_selected.zero_pairs[self.Zeros_box.currentIndex()], self.filter_selected.pole_pairs[self.Poles_Box.currentIndex()])
        self.numerador = ""
        self.denominador = ""

        if (len(self.filter_selected.stages[-1][0])) == 1:
            self.numerador = str(self.filter_selected.stages[-1][0][0])
        elif (len(self.filter_selected.stages[-1][0])) == 2:
            self.numerador = str(self.filter_selected.stages[-1][0][0]) + ".s + " + str(self.filter_selected.stages[-1][0][1])
        else:
            self.numerador = str(self.filter_selected.stages[-1][0][0]) + ".s^2 + " + str(self.filter_selected.stages[-1][0][1]) + ".s + " + str(self.filter_selected.stages[-1][0][2])

        if (len(self.filter_selected.stages[-1][1])) == 1:
            self.denominador = str(self.filter_selected.stages[-1][1][0])
        elif (len(self.filter_selected.stages[-1][1])) == 2:
            self.denominador = str(self.filter_selected.stages[-1][1][0]) + ".s + " + str(self.filter_selected.stages[-1][1][1])
        else:
            self.denominador = str(self.filter_selected.stages[-1][1][0]) + ".s^2 + " + str(self.filter_selected.stages[-1][1][1]) + ".s + " + str(self.filter_selected.stages[-1][1][2])

        self.aux_stage.label_numerador.setText(self.numerador)
        self.aux_stage.label_denominador.setText(self.denominador)
        self.aux_stage.label_n.setText(str(self.filter_selected.get_stage_n(-1)))
        self.aux_stage.label_q.setText(str(self.filter_selected.get_stage_Q(-1)))
        self.stage_array.append(self.aux_stage)
        self.Stages_Widget_2.layout().addWidget(self.aux_stage)

    def delete_stage(self):
        i = 0
        j = 0
        while i < len(self.stage_array):
            if self.stage_array[i].radioButton.isChecked() != 0:
                self.stage_array[i].hide()
                self.stage_array.pop(i)
                i = i - 1
            i = i + 1
        while j != len(self.stage_array):
            self.stage_array[j].label_2.setText("Stage " + str(j + 1))
            j = j + 1

    def selected (self):
        self.selec = []
        l = 0
        while l != len(self.stage_array):
            if self.stage_array[l].radioButton.isChecked() != 0:
                self.selec.append(l)
            l = l + 1

        self.MplWidget2.canvas.ax.clear()
        self.filter_selected.plot_combined_stages(self.MplWidget2.canvas.ax, self.selec)
        self.MplWidget2.canvas.draw()


    def superposed (self):
        self.selec = []
        l = 0
        while l != len(self.stage_array):
            if self.stage_array[l].radioButton.isChecked() != 0:
                self.selec.append(l)
            l = l + 1

        self.MplWidget2.canvas.ax.clear()
        self.filter_selected.plot_selected_stages(self.MplWidget2.canvas.ax, self.selec)
        self.MplWidget2.canvas.draw()

    def total (self):
        print("total")

        self.show_graph()


    def show_graph(self):
        print("show graph")