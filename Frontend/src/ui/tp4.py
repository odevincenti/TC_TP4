# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 773)
        Form.setStyleSheet("background:rgb(30,30,30);\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Design_Stages_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Design_Stages_button.setFont(font)
        self.Design_Stages_button.setStyleSheet("background:white;\n"
"")
        self.Design_Stages_button.setObjectName("Design_Stages_button")
        self.horizontalLayout_6.addWidget(self.Design_Stages_button)
        self.type_graph_select = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.type_graph_select.setFont(font)
        self.type_graph_select.setStyleSheet("background:white;")
        self.type_graph_select.setObjectName("type_graph_select")
        self.type_graph_select.addItem("")
        self.type_graph_select.addItem("")
        self.type_graph_select.addItem("")
        self.type_graph_select.addItem("")
        self.type_graph_select.addItem("")
        self.type_graph_select.addItem("")
        self.type_graph_select.addItem("")
        self.horizontalLayout_6.addWidget(self.type_graph_select)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_11 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:white;")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        self.filter_select = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.filter_select.setFont(font)
        self.filter_select.setStyleSheet("background:white;")
        self.filter_select.setObjectName("filter_select")
        self.filter_select.addItem("")
        self.filter_select.addItem("")
        self.filter_select.addItem("")
        self.filter_select.addItem("")
        self.filter_select.addItem("")
        self.horizontalLayout_14.addWidget(self.filter_select)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_17.addWidget(self.label_2)
        self.aproximation_select = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aproximation_select.setFont(font)
        self.aproximation_select.setStyleSheet("background:white;")
        self.aproximation_select.setObjectName("aproximation_select")
        self.aproximation_select.addItem("")
        self.aproximation_select.addItem("")
        self.aproximation_select.addItem("")
        self.aproximation_select.addItem("")
        self.aproximation_select.addItem("")
        self.horizontalLayout_17.addWidget(self.aproximation_select)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.label_12 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setStyleSheet("color:white;")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.Gain_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Gain_valor.setFont(font)
        self.Gain_valor.setStyleSheet("background:white;")
        self.Gain_valor.setObjectName("Gain_valor")
        self.horizontalLayout_15.addWidget(self.Gain_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setStyleSheet("color:white;")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_19.addWidget(self.label_15)
        self.Aa_Valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Aa_Valor.setFont(font)
        self.Aa_Valor.setStyleSheet("background:white;")
        self.Aa_Valor.setObjectName("Aa_Valor")
        self.horizontalLayout_19.addWidget(self.Aa_Valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setStyleSheet("color:white;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_20.addWidget(self.label_16)
        self.Ap_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ap_valor.setFont(font)
        self.Ap_valor.setStyleSheet("background:white;")
        self.Ap_valor.setObjectName("Ap_valor")
        self.horizontalLayout_20.addWidget(self.Ap_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_17 = QtWidgets.QLabel(self.widget_4)
        self.label_17.setStyleSheet("color:white;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_21.addWidget(self.label_17)
        self.fa_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fa_valor.setFont(font)
        self.fa_valor.setStyleSheet("background:white;")
        self.fa_valor.setObjectName("fa_valor")
        self.horizontalLayout_21.addWidget(self.fa_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setStyleSheet("color:white;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_22.addWidget(self.label_18)
        self.fp_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fp_valor.setFont(font)
        self.fp_valor.setStyleSheet("background:white;")
        self.fp_valor.setObjectName("fp_valor")
        self.horizontalLayout_22.addWidget(self.fp_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setStyleSheet("color:white;")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_23.addWidget(self.label_19)
        self.fa_mas_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fa_mas_valor.setFont(font)
        self.fa_mas_valor.setStyleSheet("background:white;")
        self.fa_mas_valor.setObjectName("fa_mas_valor")
        self.horizontalLayout_23.addWidget(self.fa_mas_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setStyleSheet("color:white;")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_24.addWidget(self.label_20)
        self.fa_menos_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fa_menos_valor.setFont(font)
        self.fa_menos_valor.setStyleSheet("background:white;")
        self.fa_menos_valor.setObjectName("fa_menos_valor")
        self.horizontalLayout_24.addWidget(self.fa_menos_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_21 = QtWidgets.QLabel(self.widget_4)
        self.label_21.setStyleSheet("color:white;")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_25.addWidget(self.label_21)
        self.fp_mas_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fp_mas_valor.setFont(font)
        self.fp_mas_valor.setStyleSheet("background:white;")
        self.fp_mas_valor.setObjectName("fp_mas_valor")
        self.horizontalLayout_25.addWidget(self.fp_mas_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_22 = QtWidgets.QLabel(self.widget_4)
        self.label_22.setStyleSheet("color:white;")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_26.addWidget(self.label_22)
        self.fp_menos_valor = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fp_menos_valor.setFont(font)
        self.fp_menos_valor.setStyleSheet("background:white;")
        self.fp_menos_valor.setObjectName("fp_menos_valor")
        self.horizontalLayout_26.addWidget(self.fp_menos_valor)
        self.verticalLayout_12.addLayout(self.horizontalLayout_26)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem)
        self.verticalLayout_11.addWidget(self.widget_4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Graph_Widget = QtWidgets.QWidget(Form)
        self.Graph_Widget.setStyleSheet("background:blue;")
        self.Graph_Widget.setObjectName("Graph_Widget")
        self.verticalLayout_13.addWidget(self.Graph_Widget)
        self.verticalLayout_9.addLayout(self.verticalLayout_13)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_13.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.N_slider = QtWidgets.QSlider(Form)
        self.N_slider.setMinimum(1)
        self.N_slider.setMaximum(9)
        self.N_slider.setOrientation(QtCore.Qt.Horizontal)
        self.N_slider.setObjectName("N_slider")
        self.horizontalLayout_11.addWidget(self.N_slider)
        self.N_box = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.N_box.setFont(font)
        self.N_box.setStyleSheet("background:white;")
        self.N_box.setMinimum(1)
        self.N_box.setMaximum(20)
        self.N_box.setObjectName("N_box")
        self.horizontalLayout_11.addWidget(self.N_box)
        self.N_check = QtWidgets.QCheckBox(Form)
        self.N_check.setText("")
        self.N_check.setObjectName("N_check")
        self.horizontalLayout_11.addWidget(self.N_check)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.Q_slider = QtWidgets.QSlider(Form)
        self.Q_slider.setMinimum(1)
        self.Q_slider.setMaximum(20)
        self.Q_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Q_slider.setObjectName("Q_slider")
        self.horizontalLayout_12.addWidget(self.Q_slider)
        self.Q_box = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Q_box.setFont(font)
        self.Q_box.setStyleSheet("Background:white;")
        self.Q_box.setMinimum(1)
        self.Q_box.setMaximum(20)
        self.Q_box.setObjectName("Q_box")
        self.horizontalLayout_12.addWidget(self.Q_box)
        self.Q_check = QtWidgets.QCheckBox(Form)
        self.Q_check.setText("")
        self.Q_check.setObjectName("Q_check")
        self.horizontalLayout_12.addWidget(self.Q_check)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_10.addLayout(self.horizontalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_14 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:white;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_18.addWidget(self.label_14)
        self.Denom_slider = QtWidgets.QSlider(Form)
        self.Denom_slider.setMinimum(0)
        self.Denom_slider.setMaximum(100)
        self.Denom_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Denom_slider.setObjectName("Denom_slider")
        self.horizontalLayout_18.addWidget(self.Denom_slider)
        self.Denom_box = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Denom_box.setFont(font)
        self.Denom_box.setStyleSheet("background:white;")
        self.Denom_box.setMinimum(0)
        self.Denom_box.setMaximum(100)
        self.Denom_box.setObjectName("Denom_box")
        self.horizontalLayout_18.addWidget(self.Denom_box)
        self.Denom_check = QtWidgets.QCheckBox(Form)
        self.Denom_check.setText("")
        self.Denom_check.setObjectName("Denom_check")
        self.horizontalLayout_18.addWidget(self.Denom_check)
        self.verticalLayout_15.addLayout(self.horizontalLayout_18)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Curve_List_Select = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Curve_List_Select.setFont(font)
        self.Curve_List_Select.setStyleSheet("background:white;")
        self.Curve_List_Select.setObjectName("Curve_List_Select")
        self.horizontalLayout_2.addWidget(self.Curve_List_Select)
        self.Edit_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Edit_button.setFont(font)
        self.Edit_button.setStyleSheet("background:white;")
        self.Edit_button.setObjectName("Edit_button")
        self.horizontalLayout_2.addWidget(self.Edit_button)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.add_curve_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_curve_button.setFont(font)
        self.add_curve_button.setStyleSheet("background:rgb(0,255,0);\n"
"color:white;")
        self.add_curve_button.setObjectName("add_curve_button")
        self.verticalLayout_14.addWidget(self.add_curve_button)
        self.remove_curve_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.remove_curve_button.setFont(font)
        self.remove_curve_button.setStyleSheet("background:rgb(255,0,0);\n"
"color:white;")
        self.remove_curve_button.setObjectName("remove_curve_button")
        self.verticalLayout_14.addWidget(self.remove_curve_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TP4 - GRUPO 3"))
        self.Design_Stages_button.setText(_translate("Form", "DESIGN STAGES"))
        self.type_graph_select.setItemText(0, _translate("Form", "Module"))
        self.type_graph_select.setItemText(1, _translate("Form", "Phase"))
        self.type_graph_select.setItemText(2, _translate("Form", "Attenuation"))
        self.type_graph_select.setItemText(3, _translate("Form", "Normalized Attenuation"))
        self.type_graph_select.setItemText(4, _translate("Form", "Group Delay"))
        self.type_graph_select.setItemText(5, _translate("Form", "Qmáx"))
        self.type_graph_select.setItemText(6, _translate("Form", "Zeros and Poles"))
        self.label_11.setText(_translate("Form", "FILTER TYPE"))
        self.filter_select.setItemText(0, _translate("Form", "LP"))
        self.filter_select.setItemText(1, _translate("Form", "HP"))
        self.filter_select.setItemText(2, _translate("Form", "BP"))
        self.filter_select.setItemText(3, _translate("Form", "BR"))
        self.filter_select.setItemText(4, _translate("Form", "Group Delay"))
        self.label_2.setText(_translate("Form", "APPROXIMATION"))
        self.aproximation_select.setItemText(0, _translate("Form", "Butterworth"))
        self.aproximation_select.setItemText(1, _translate("Form", "Bessel"))
        self.aproximation_select.setItemText(2, _translate("Form", "Chebycheff ll"))
        self.aproximation_select.setItemText(3, _translate("Form", "Legendre"))
        self.aproximation_select.setItemText(4, _translate("Form", "Gauss"))
        self.label_12.setText(_translate("Form", "PARAMETERS"))
        self.label_13.setText(_translate("Form", "Gain [dB]"))
        self.label_15.setText(_translate("Form", "Aa [dB]"))
        self.label_16.setText(_translate("Form", "Ap [dB]"))
        self.label_17.setText(_translate("Form", "fa [Hz]"))
        self.label_18.setText(_translate("Form", "fp [Hz]"))
        self.label_19.setText(_translate("Form", "fa+ [Hz]"))
        self.label_20.setText(_translate("Form", "fa- [Hz]"))
        self.label_21.setText(_translate("Form", "fp+ [Hz]"))
        self.label_22.setText(_translate("Form", "fp- [Hz]"))
        self.label_9.setText(_translate("Form", "N"))
        self.label_10.setText(_translate("Form", "Q"))
        self.label_14.setText(_translate("Form", "Denom."))
        self.Edit_button.setText(_translate("Form", "EDIT"))
        self.add_curve_button.setText(_translate("Form", "+"))
        self.remove_curve_button.setText(_translate("Form", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())