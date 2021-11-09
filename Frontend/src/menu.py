import numpy as np
from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4 import Ui_Form
from Frontend.src.edit_window import EditWindow
from Frontend.src.tp4_stages import Stages
from back.backend import FilterSpace, FilterType, ApproxType

class MainWindowQ (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.error = 0
        self.cant_curvas = 0
        self.fs = FilterSpace()

        self.Qmax = 0
        self.Nmaxmin = 0
        self.denom = 0

        self.Qmax_valor = 0
        self.denom_valor = 0

        #HIDESSSS
        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()
        self.label_24.hide()
        self.label_25.hide()

        self.fa_mas_valor.hide()
        self.fa_menos_valor.hide()
        self.fp_mas_valor.hide()
        self.fp_menos_valor.hide()
        self.GD_value.hide()
        self.tolerance_value.hide()

        self.Denom_slider.hide()
        self.Denom_box.hide()
        self.Q_slider.hide()
        self.Q_box.hide()

        self.label_23.hide()
        self.N_max_slider.hide()
        self.N_max_box.hide()
        self.label_9.setText("N")
        self.label_3.hide()

        self.aproximation_select_2.hide()


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

        self.Edit_button.clicked.connect(self.edit_curve)

        self.Design_Stages_button.clicked.connect(self.Design_Stages)


        #GRAPHHHHHH
        #crear el box para la toolbar
        self.MplWidget.show_toolbar(self.Toolbar1)




    # FUNCIONESSSS

    def filter_change(self, value):
        if value == 0 or value == 1:
            self.label_19.hide()
            self.label_20.hide()
            self.label_21.hide()
            self.label_22.hide()
            self.label_24.hide()
            self.label_25.hide()
            self.fa_mas_valor.hide()
            self.fa_menos_valor.hide()
            self.fp_mas_valor.hide()
            self.fp_menos_valor.hide()
            self.GD_value.hide()
            self.tolerance_value.hide()
            self.aproximation_select_2.hide()
            self.label_15.show()
            self.label_16.show()
            self.Aa_Valor.show()
            self.Ap_valor.show()
            self.label_17.show()
            self.label_18.show()
            self.fp_valor.show()
            self.fa_valor.show()
            self.aproximation_select.show()


        elif value == 2 or value == 3:
            self.label_17.hide()
            self.label_18.hide()
            self.fa_valor.hide()
            self.fp_valor.hide()
            self.label_24.hide()
            self.label_25.hide()
            self.GD_value.hide()
            self.tolerance_value.hide()
            self.aproximation_select_2.hide()
            self.label_15.show()
            self.label_16.show()
            self.label_19.show()
            self.label_20.show()
            self.label_21.show()
            self.label_22.show()
            self.Aa_Valor.show()
            self.Ap_valor.show()
            self.fa_mas_valor.show()
            self.fa_menos_valor.show()
            self.fp_mas_valor.show()
            self.fp_menos_valor.show()
            self.aproximation_select.show()


        elif value == 4:
            self.label_15.hide()
            self.label_16.hide()
            self.label_17.hide()
            self.fa_valor.hide()
            self.label_19.hide()
            self.label_20.hide()
            self.label_21.hide()
            self.label_22.hide()
            self.Aa_Valor.hide()
            self.Ap_valor.hide()
            self.fa_mas_valor.hide()
            self.fa_menos_valor.hide()
            self.fp_mas_valor.hide()
            self.fp_menos_valor.hide()
            self.aproximation_select.hide()
            self.label_24.show()
            self.label_25.show()
            self.GD_value.show()
            self.tolerance_value.show()
            self.aproximation_select_2.show()


    def aproximation_change(self, value):
        if value == 2:
            self.label_14.hide()
            self.Denom_check.hide()
            self.Denom_slider.hide()
            self.Denom_box.hide()
        else:
            self.label_14.show()
            self.Denom_check.show()

    def type_graph_change(self, value):
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


    def N_check_state (self, value):
        if value == 0:
            self.label_23.hide()
            self.N_max_slider.hide()
            self.N_max_box.hide()
            self.label_9.setText("N")
            self.Nmaxmin = 0
        else:
            self.label_23.show()
            self.N_min_slider_2.show()
            self.N_min_box_2.show()
            self.N_max_slider.show()
            self.N_max_box.show()
            self.label_9.setText("Nmin")
            self.Nmaxmin = 1

    def Q_check_state (self, value):
        if value == 0:
            self.Q_slider.hide()
            self.Q_box.hide()
            self.Qmax = 0
        else:
            self.Q_slider.show()
            self.Q_box.show()
            self.Qmax = 1

    def Denom_check_state (self, value):
        if value == 0:
            self.Denom_slider.hide()
            self.Denom_box.hide()
            self.denom = 0
        else:
            self.Denom_slider.show()
            self.Denom_box.show()
            self.denom = 1


    def create_curve(self):
        print("add")
        if self.Qmax == 0:
            self.Qmax_valor = None
            self.Qmax_text = "Auto."
        else:
            self.Qmax_valor = self.Q_box.value()
            self.Qmax_text = str(self.Q_box.value())
        if self.denom == 0:
            self.denom_valor = 0
            self.denom_text = "Auto."
        else:
            self.denom_valor = self.Denom_box.value()
            self.denom_text = str(self.Denom_box.value())

        if self.filter_select.currentIndex() == 0 or self.filter_select.currentIndex() == 1:
            if self.Nmaxmin == 0:
                if (self.fs.addFilter(self.filter_select.currentIndex(), self.aproximation_select.currentIndex(), (self.fp_valor.value()) * 2 * np.pi, (self.fa_valor.value()) * 2 * np.pi, self.Ap_valor.value(), self.Aa_Valor.value(), self.denom_valor, self.N_min_box_2.value(), None, None, None, self.Qmax_valor, None, None, None) == ""):
                    self.error = 0
                else:
                    self.error = 1
            elif self.Nmaxmin == 1:
                if (self.fs.addFilter(self.filter_select.currentIndex(), self.aproximation_select.currentIndex(),
                                      (self.fp_valor.value()) * 2 * np.pi, (self.fa_valor.value()) * 2 * np.pi, self.Ap_valor.value(), self.Aa_Valor.value(), self.denom_valor,
                                      None, self.N_min_box_2.value(), self.N_max_box.value(), None, self.Qmax_valor, None,
                                      None, None) == ""):
                    self.error = 0
                else:
                    self.error = 1


        elif self.filter_select.currentIndex() == 4:
            if self.Nmaxmin == 0:
                if (self.fs.addFilter(self.filter_select.currentIndex(), self.aproximation_select_2.currentIndex(), (self.fp_valor.value()) * 2 * np.pi, None, None, None, self.denom_valor, self.N_min_box_2.value(), None, None, None, self.Qmax_valor, None, self.GD_value.value(), self.tolerance_value.value()) == ""):
                    self.error = 0
                else:
                    self.error = 1
            elif self.Nmaxmin == 1:
                if (self.fs.addFilter(self.filter_select.currentIndex(), self.aproximation_select_2.currentIndex(),
                                      (self.fp_valor.value()) * 2 * np.pi, None, None, None, self.denom_valor,
                                      None, self.N_min_box_2.value(), self.N_max_box, None, self.Qmax_valor, None,
                                      self.GD_value.value(), self.tolerance_value.value()) == ""):
                    self.error = 0
                else:
                    self.error = 1

        if self.error == 0:
            self.label_3.hide()
            if self.Nmaxmin == 0:
                self.Curve_List_Select.addItems(('Curve' + ":" + (self.aproximation_select.currentText()) + "__" + (
                    self.filter_select.currentText()) + "__N:" + str(self.N_min_box_2.value()) + "__Qmax:" + (
                    self.Qmax_text) + "__Denom:" + (
                    self.denom_text)).split())
            elif self.Nmaxmin == 1:
                self.Curve_List_Select.addItems(('Curve' + ":" + (self.aproximation_select.currentText()) + "__" + (
                    self.filter_select.currentText()) + "__Nmin:" + str(self.N_min_box_2.value()) + "__Nmax:" + str(self.N_max_box.value()) + "__Qmax:" + (
                                                     self.Qmax_text) + "__Denom:" + (
                                                     self.denom_text)).split())
            self.cant_curvas = self.cant_curvas + 1
            self.label_3.hide()
        else:
            print("ERROR")
            self.label_3.show()
            self.error = 0

    def remove_curve(self):
        print("remove")
        if self.cant_curvas > 0:
            self.fs.delFilter(self.Curve_List_Select.currentIndex())
            self.Curve_List_Select.removeItem(self.Curve_List_Select.currentIndex())
            self.cant_curvas = self.cant_curvas - 1

    def edit_curve(self):
        print("edit")
        if self.cant_curvas > 0:
            self.edit_wind = EditWindow()

    def Design_Stages (self):
        print("second")
        if self.cant_curvas > 0:
            self.stages = Stages()











