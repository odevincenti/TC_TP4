# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp4_stages.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1143, 844)
        Form.setStyleSheet("background: rgb(30,30,30)")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.PyZ_Widget = MplWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PyZ_Widget.sizePolicy().hasHeightForWidth())
        self.PyZ_Widget.setSizePolicy(sizePolicy)
        self.PyZ_Widget.setMaximumSize(QtCore.QSize(300, 400))
        self.PyZ_Widget.setStyleSheet("background:pink;")
        self.PyZ_Widget.setObjectName("PyZ_Widget")
        self.horizontalLayout_14.addWidget(self.PyZ_Widget)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.Zeros_box = QtWidgets.QComboBox(Form)
        self.Zeros_box.setStyleSheet("background:rgb(30,30,30);\n"
"color:white;")
        self.Zeros_box.setObjectName("Zeros_box")
        self.verticalLayout_6.addWidget(self.Zeros_box)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.Poles_Box = QtWidgets.QComboBox(Form)
        self.Poles_Box.setStyleSheet("background:rgb(30,30,30);\n"
"color:white;")
        self.Poles_Box.setObjectName("Poles_Box")
        self.verticalLayout_6.addWidget(self.Poles_Box)
        self.Create_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Create_button.setFont(font)
        self.Create_button.setStyleSheet("background:white;")
        self.Create_button.setObjectName("Create_button")
        self.verticalLayout_6.addWidget(self.Create_button)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.MplWidget2 = MplWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget2.sizePolicy().hasHeightForWidth())
        self.MplWidget2.setSizePolicy(sizePolicy)
        self.MplWidget2.setMaximumSize(QtCore.QSize(700, 500))
        self.MplWidget2.setStyleSheet("background:blue;")
        self.MplWidget2.setObjectName("MplWidget2")
        self.verticalLayout_14.addWidget(self.MplWidget2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem2)
        self.Toolbar2 = QtWidgets.QVBoxLayout()
        self.Toolbar2.setObjectName("Toolbar2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Toolbar2.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.Toolbar2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_5 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line_5.setFont(font)
        self.line_5.setStyleSheet("color:white;")
        self.line_5.setLineWidth(1)
        self.line_5.setMidLineWidth(5)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_8.addWidget(self.line_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_6 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line_6.setFont(font)
        self.line_6.setStyleSheet("color:white;")
        self.line_6.setLineWidth(1)
        self.line_6.setMidLineWidth(5)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_4.addWidget(self.line_6)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.Select_button_1 = QtWidgets.QRadioButton(Form)
        self.Select_button_1.setText("")
        self.Select_button_1.setObjectName("Select_button_1")
        self.horizontalLayout_4.addWidget(self.Select_button_1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setStyleSheet("color:white;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.Select_button_2 = QtWidgets.QRadioButton(Form)
        self.Select_button_2.setText("")
        self.Select_button_2.setObjectName("Select_button_2")
        self.horizontalLayout_4.addWidget(self.Select_button_2)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.Select_button_3 = QtWidgets.QRadioButton(Form)
        self.Select_button_3.setText("")
        self.Select_button_3.setObjectName("Select_button_3")
        self.horizontalLayout_4.addWidget(self.Select_button_3)
        self.line_7 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line_7.setFont(font)
        self.line_7.setStyleSheet("color:white;")
        self.line_7.setLineWidth(1)
        self.line_7.setMidLineWidth(5)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_4.addWidget(self.line_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.line_8 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line_8.setFont(font)
        self.line_8.setStyleSheet("color:white;")
        self.line_8.setLineWidth(1)
        self.line_8.setMidLineWidth(5)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_8.addWidget(self.line_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_13.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_23 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:white;\n"
"")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23)
        self.Q_valor = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Q_valor.setFont(font)
        self.Q_valor.setStyleSheet("color:white;\n"
"")
        self.Q_valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Q_valor.setObjectName("Q_valor")
        self.horizontalLayout_5.addWidget(self.Q_valor)
        self.label_25 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:white;\n"
"")
        self.label_25.setText("")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_5.addWidget(self.label_25)
        self.label_29 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:white;\n"
"")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_5.addWidget(self.label_29)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_26 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:white;\n"
"")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_7.addWidget(self.label_26)
        self.fo_valor = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.fo_valor.setFont(font)
        self.fo_valor.setStyleSheet("color:white;\n"
"")
        self.fo_valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fo_valor.setObjectName("fo_valor")
        self.horizontalLayout_7.addWidget(self.fo_valor)
        self.label_28 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:white;\n"
"")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_7.addWidget(self.label_28)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_27 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:white;\n"
"")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_15.addWidget(self.label_27)
        self.k_valor = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.k_valor.setFont(font)
        self.k_valor.setStyleSheet("color:white;\n"
"")
        self.k_valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.k_valor.setObjectName("k_valor")
        self.horizontalLayout_15.addWidget(self.k_valor)
        self.label_30 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:white;\n"
"")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_15.addWidget(self.label_30)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.autobutton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.autobutton.setFont(font)
        self.autobutton.setStyleSheet("background:white;")
        self.autobutton.setObjectName("autobutton")
        self.verticalLayout_10.addWidget(self.autobutton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(1000, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 480, 330))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Stages_Widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.Stages_Widget_2.setStyleSheet("background:rgb(30,30,30);")
        self.Stages_Widget_2.setObjectName("Stages_Widget_2")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.Stages_Widget_2)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_Stages = QtWidgets.QWidget(self.Stages_Widget_2)
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addWidget(self.widget_Stages)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.addWidget(self.Stages_Widget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_16.addWidget(self.scrollArea)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.delete_stage_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_stage_button.setFont(font)
        self.delete_stage_button.setStyleSheet("background:red;\n"
"color:white;")
        self.delete_stage_button.setObjectName("delete_stage_button")
        self.horizontalLayout.addWidget(self.delete_stage_button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TP4 - GRUPO 3 - DESIGN STAGES"))
        self.label_4.setText(_translate("Form", "Zeros"))
        self.label_5.setText(_translate("Form", "Poles"))
        self.Create_button.setText(_translate("Form", "Create"))
        self.label_8.setText(_translate("Form", "Combined"))
        self.label_11.setText(_translate("Form", "Superposed"))
        self.label_12.setText(_translate("Form", "Total"))
        self.label_23.setText(_translate("Form", "Q:"))
        self.Q_valor.setText(_translate("Form", "N/A"))
        self.label_29.setText(_translate("Form", "Hz"))
        self.label_26.setText(_translate("Form", "fo:"))
        self.fo_valor.setText(_translate("Form", "N/A"))
        self.label_28.setText(_translate("Form", "Hz"))
        self.label_27.setText(_translate("Form", "k:"))
        self.k_valor.setText(_translate("Form", "N/A"))
        self.label_30.setText(_translate("Form", "V/V"))
        self.autobutton.setText(_translate("Form", "Auto"))
        self.label_2.setText(_translate("Form", "Stage 1"))
        self.label_3.setText(_translate("Form", "H(s) = "))
        self.label_6.setText(_translate("Form", "n = "))
        self.label_7.setText(_translate("Form", "Q = "))
        self.delete_stage_button.setText(_translate("Form", "DELETE"))
from Frontend.src.mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
