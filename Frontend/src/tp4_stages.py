from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4_stages import Ui_Form
from Frontend.src.mplwidget import MplWidget

class Stages (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()

        #HIDESSSSS
        self.Q_valor.hide()
        self.fo_valor.hide()
        self.DR_valor.hide()
        self.label_28.hide()
        self.label_31.hide()

