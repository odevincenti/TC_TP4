from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4 import Ui_Form
from Frontend.src.mplwidget import MplWidget
from Frontend.src.edit_window import EditWindow

class MainWindowQ (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.error = 0
        self.cant_curvas = 0

        #HIDESSSS
        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()

        self.fa_mas_valor.hide()
        self.fa_menos_valor.hide()
        self.fp_mas_valor.hide()
        self.fp_menos_valor.hide()

        self.Denom_slider.hide()
        self.Denom_box.hide()
        self.Q_slider.hide()
        self.Q_box.hide()


        self.label_23.hide()
        self.N_max_slider.hide()
        self.N_max_box.hide()
        self.label_9.setText("N")


        #BOXESSSSSSS
        self.filter_select.currentIndexChanged.connect(self.filter_change)
        self.aproximation_select.currentIndexChanged.connect(self.aproximation_change)
        self.type_graph_select.currentIndexChanged.connect(self.type_graph_change)


        #CHECK BOXESSSSS
        self.N_check.stateChanged.connect(self.N_check_state)
        self.Q_check.stateChanged.connect(self.Q_check_state)
        self.Denom_check.stateChanged.connect(self.Denom_check_state)


        #BUTTONSSSS
        self.add_curve_button.clicked.connect(self.create_curve)
        self.remove_curve_button.clicked.connect(self.remove_curve)

        self.Edit_button.clicked.connect(self.edit_Stages)

        self.Design_Stages_button.clicked.connect(self.Design_Stages)


        #GRAPHHHHHH
        #self.MplWidget.show_toolbar(self.Toolbar1)



    # FUNCIONESSSS

    def filter_change(self, value):
        if value == 0 or value == 1:
            self.label_19.hide()
            self.label_20.hide()
            self.label_21.hide()
            self.label_22.hide()
            self.fa_mas_valor.hide()
            self.fa_menos_valor.hide()
            self.fp_mas_valor.hide()
            self.fp_menos_valor.hide()


        elif value == 2 or value == 3:
            self.label_19.show()
            self.label_20.show()
            self.label_21.show()
            self.label_22.show()
            self.fa_mas_valor.show()
            self.fa_menos_valor.show()
            self.fp_mas_valor.show()
            self.fp_menos_valor.show()

    def aproximation_change(self,value):
        if value == 2:
            self.label_14.hide()
            self.Denom_check.hide()
            self.Denom_slider.hide()
            self.Denom_box.hide()
        else:
            self.label_14.show()
            self.Denom_check.show()

    def type_graph_change(self,value):
        if value == 0:
            print(0)
        elif value == 1:
            print(1)
        elif value == 2:
            print(2)
        elif value == 3:
            print(3)
        elif value == 4:
            print(4)
        elif value == 5:
            print(5)
        elif value == 6:
            print(6)


    def N_check_state (self,value):
        if value == 0:
            self.label_23.hide()
            self.N_max_slider.hide()
            self.N_max_box.hide()
            self.label_9.setText("N")
        else:
            self.label_23.show()
            self.N_min_slider_2.show()
            self.N_min_box_2.show()
            self.N_max_slider.show()
            self.N_max_box.show()
            self.label_9.setText("Nmin")

    def Q_check_state (self,value):
        if value == 0:
            self.Q_slider.hide()
            self.Q_box.hide()
        else:
            self.Q_slider.show()
            self.Q_box.show()

    def Denom_check_state (self,value):
        if value == 0:
            self.Denom_slider.hide()
            self.Denom_box.hide()
        else:
            self.Denom_slider.show()
            self.Denom_box.show()


    def create_curve(self):
        if self.error == 0:
            self.Curve_List_Select.addItems(('Curve' + ":" + (self.aproximation_select.currentText()) + "__" + (self.filter_select.currentText())).split())
            self.cant_curvas = self.cant_curvas + 1


    def remove_curve(self):
        if self.cant_curvas > 0:
            self.Curve_List_Select.removeItem(self.Curve_List_Select.currentIndex())
            self.cant_curvas = self.cant_curvas - 1

    def edit_Stages(self):
        print("edit")
        if self.cant_curvas > 0:
            self.edit_wind = EditWindow()

    def Design_Stages (self):
        print("second")










