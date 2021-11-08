from PyQt5.QtWidgets import QWidget
from Frontend.src.ui.tp4_stages import Ui_Form
from Frontend.src.mplwidget import MplWidget
from Frontend.src.edit_window import EditWindow

class Stages (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()