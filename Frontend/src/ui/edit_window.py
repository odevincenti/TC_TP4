# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(764, 607)
        Form.setStyleSheet("background:rgb(90,90,90);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.GoBack_Button_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.GoBack_Button_2.setFont(font)
        self.GoBack_Button_2.setStyleSheet("background:white;\n"
"")
        self.GoBack_Button_2.setObjectName("GoBack_Button_2")
        self.horizontalLayout_3.addWidget(self.GoBack_Button_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:white;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.N_check_2 = QtWidgets.QCheckBox(self.widget_4)
        self.N_check_2.setText("")
        self.N_check_2.setObjectName("N_check_2")
        self.horizontalLayout_13.addWidget(self.N_check_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.N_min_slider_3 = QtWidgets.QSlider(self.widget_4)
        self.N_min_slider_3.setMinimum(1)
        self.N_min_slider_3.setMaximum(20)
        self.N_min_slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.N_min_slider_3.setObjectName("N_min_slider_3")
        self.horizontalLayout_13.addWidget(self.N_min_slider_3)
        self.N_min_box_3 = QtWidgets.QSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.N_min_box_3.setFont(font)
        self.N_min_box_3.setStyleSheet("background:white;")
        self.N_min_box_3.setMinimum(1)
        self.N_min_box_3.setMaximum(20)
        self.N_min_box_3.setObjectName("N_min_box_3")
        self.horizontalLayout_13.addWidget(self.N_min_box_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_23 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:white;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_16.addWidget(self.label_23)
        self.Q_check_2 = QtWidgets.QCheckBox(self.widget_4)
        self.Q_check_2.setText("")
        self.Q_check_2.setObjectName("Q_check_2")
        self.horizontalLayout_16.addWidget(self.Q_check_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.Q_slider_2 = QtWidgets.QSlider(self.widget_4)
        self.Q_slider_2.setMinimum(1)
        self.Q_slider_2.setMaximum(20)
        self.Q_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.Q_slider_2.setObjectName("Q_slider_2")
        self.horizontalLayout_16.addWidget(self.Q_slider_2)
        self.Q_box_2 = QtWidgets.QSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Q_box_2.setFont(font)
        self.Q_box_2.setStyleSheet("Background:white;")
        self.Q_box_2.setMinimum(1)
        self.Q_box_2.setMaximum(20)
        self.Q_box_2.setObjectName("Q_box_2")
        self.horizontalLayout_16.addWidget(self.Q_box_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_10.addLayout(self.verticalLayout_13)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_10.addLayout(self.horizontalLayout_18)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_24 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:white;")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_27.addWidget(self.label_24)
        self.N_max_slider = QtWidgets.QSlider(self.widget_4)
        self.N_max_slider.setMinimum(1)
        self.N_max_slider.setMaximum(20)
        self.N_max_slider.setOrientation(QtCore.Qt.Horizontal)
        self.N_max_slider.setObjectName("N_max_slider")
        self.horizontalLayout_27.addWidget(self.N_max_slider)
        self.N_max_box = QtWidgets.QSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.N_max_box.setFont(font)
        self.N_max_box.setStyleSheet("background:white;")
        self.N_max_box.setMinimum(1)
        self.N_max_box.setMaximum(20)
        self.N_max_box.setObjectName("N_max_box")
        self.horizontalLayout_27.addWidget(self.N_max_box)
        self.verticalLayout_15.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_25 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:white;")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_28.addWidget(self.label_25)
        self.Denom_check = QtWidgets.QCheckBox(self.widget_4)
        self.Denom_check.setText("")
        self.Denom_check.setObjectName("Denom_check")
        self.horizontalLayout_28.addWidget(self.Denom_check)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem5)
        self.Denom_slider = QtWidgets.QSlider(self.widget_4)
        self.Denom_slider.setMinimum(0)
        self.Denom_slider.setMaximum(100)
        self.Denom_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Denom_slider.setObjectName("Denom_slider")
        self.horizontalLayout_28.addWidget(self.Denom_slider)
        self.Denom_box = QtWidgets.QSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Denom_box.setFont(font)
        self.Denom_box.setStyleSheet("background:white;")
        self.Denom_box.setMinimum(0)
        self.Denom_box.setMaximum(100)
        self.Denom_box.setObjectName("Denom_box")
        self.horizontalLayout_28.addWidget(self.Denom_box)
        self.verticalLayout_15.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_10.addLayout(self.verticalLayout_15)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_12.addWidget(self.pushButton)
        self.verticalLayout_11.addWidget(self.widget_4)
        self.horizontalLayout.addLayout(self.verticalLayout_11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.GoBack_Button_2.setText(_translate("Form", "<-"))
        self.label_3.setText(_translate("Form", "EDIT CURVE"))
        self.label_11.setText(_translate("Form", "FILTER TYPE"))
        self.filter_select.setItemText(0, _translate("Form", "Low-Pass"))
        self.filter_select.setItemText(1, _translate("Form", "High-Pass"))
        self.filter_select.setItemText(2, _translate("Form", "Band-Pass"))
        self.filter_select.setItemText(3, _translate("Form", "Band-Reject"))
        self.filter_select.setItemText(4, _translate("Form", "Group-Delay"))
        self.label_2.setText(_translate("Form", "APPROXIMATION"))
        self.aproximation_select.setItemText(0, _translate("Form", "Butterworth"))
        self.aproximation_select.setItemText(1, _translate("Form", "Chebycheff_l"))
        self.aproximation_select.setItemText(2, _translate("Form", "Chebycheff_ll"))
        self.aproximation_select.setItemText(3, _translate("Form", "Legendre"))
        self.aproximation_select.setItemText(4, _translate("Form", "Cauer"))
        self.aproximation_select.setItemText(5, _translate("Form", "Bessel"))
        self.aproximation_select.setItemText(6, _translate("Form", "Gauss"))
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
        self.label_14.setText(_translate("Form", "Nmin"))
        self.label_23.setText(_translate("Form", "Qmax"))
        self.label_24.setText(_translate("Form", "Nmax"))
        self.label_25.setText(_translate("Form", "Denom."))
        self.pushButton.setText(_translate("Form", "APPLY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
