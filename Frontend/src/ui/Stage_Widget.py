# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Stage_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1092, 535)
        Form.setStyleSheet("background:rgb(30,30,30);\n"
"")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_Stages = QtWidgets.QWidget(Form)
        self.widget_Stages.setStyleSheet("")
        self.widget_Stages.setObjectName("widget_Stages")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_Stages)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_Stages)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.radioButton = QtWidgets.QRadioButton(self.widget_Stages)
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_5.addWidget(self.radioButton)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.widget_Stages)
        self.label_3.setStyleSheet("color:white\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_numerador = QtWidgets.QLabel(self.widget_Stages)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numerador.setFont(font)
        self.label_numerador.setStyleSheet("color:white")
        self.label_numerador.setText("")
        self.label_numerador.setAlignment(QtCore.Qt.AlignCenter)
        self.label_numerador.setObjectName("label_numerador")
        self.verticalLayout_12.addWidget(self.label_numerador)
        self.line_ecuacion = QtWidgets.QFrame(self.widget_Stages)
        self.line_ecuacion.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_ecuacion.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_ecuacion.setObjectName("line_ecuacion")
        self.verticalLayout_12.addWidget(self.line_ecuacion)
        self.label_denominador = QtWidgets.QLabel(self.widget_Stages)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_denominador.setFont(font)
        self.label_denominador.setStyleSheet("color:white")
        self.label_denominador.setText("")
        self.label_denominador.setAlignment(QtCore.Qt.AlignCenter)
        self.label_denominador.setObjectName("label_denominador")
        self.verticalLayout_12.addWidget(self.label_denominador)
        self.horizontalLayout_12.addLayout(self.verticalLayout_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.line_ecuacion_2 = QtWidgets.QFrame(self.widget_Stages)
        self.line_ecuacion_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_ecuacion_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_ecuacion_2.setObjectName("line_ecuacion_2")
        self.verticalLayout_7.addWidget(self.line_ecuacion_2)
        self.line_ecuacion_3 = QtWidgets.QFrame(self.widget_Stages)
        self.line_ecuacion_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_ecuacion_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_ecuacion_3.setObjectName("line_ecuacion_3")
        self.verticalLayout_7.addWidget(self.line_ecuacion_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.widget_Stages)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_q = QtWidgets.QLabel(self.widget_Stages)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_q.setFont(font)
        self.label_q.setStyleSheet("color:white")
        self.label_q.setText("")
        self.label_q.setAlignment(QtCore.Qt.AlignCenter)
        self.label_q.setObjectName("label_q")
        self.gridLayout.addWidget(self.label_q, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_Stages)
        self.label_7.setStyleSheet("color:white")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_n = QtWidgets.QLabel(self.widget_Stages)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_n.setFont(font)
        self.label_n.setStyleSheet("color:white")
        self.label_n.setText("")
        self.label_n.setAlignment(QtCore.Qt.AlignCenter)
        self.label_n.setObjectName("label_n")
        self.gridLayout.addWidget(self.label_n, 1, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addWidget(self.widget_Stages)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Stage 1"))
        self.label_3.setText(_translate("Form", "H(s) = "))
        self.label_6.setText(_translate("Form", "n = "))
        self.label_7.setText(_translate("Form", "Q = "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
