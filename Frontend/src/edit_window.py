from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.edit_window import Ui_Form



class EditWindow (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()

        self.error = 0
        self.cant_curvas = 0

        self.Qmax = 0
        self.Nmaxmin = 0
        self.denom = 0

        self.Qmax_valor = 0
        self.denom_valor = 0


        #HIDEEEEE
        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()
        self.label_26.hide()
        self.label_27.hide()

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

        # BOXESSSSSSS
        self.filter_select.currentIndexChanged.connect(self.filter_change)
        self.aproximation_select.currentIndexChanged.connect(self.aproximation_change)
        self.type_graph_select.currentIndexChanged.connect(self.type_graph_change)

        # CHECK BOXESSSSS
        self.N_check.stateChanged.connect(self.N_check_state)
        self.Q_check.stateChanged.connect(self.Q_check_state)
        self.Denom_check.stateChanged.connect(self.Denom_check_state)

        # BUTTONSSSS
        self.pushButton.clicked.connect(self.apply_curve)


        # GRAPHHHHHH
        # crear el box para la toolbar
        self.MplWidget.show_toolbar(self.Toolbar2)

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

    def apply_curve (self):
        print("apply")