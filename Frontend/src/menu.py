
from PyQt5.QtWidgets import QWidget

from Frontend.src.ui.tp4 import Ui_Form


class MainWindowQ (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)

        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()

        self.fa_mas_valor.hide()
        self.fa_menos_valor.hide()
        self.fp_mas_valor.hide()
        self.fp_menos_valor.hide()




