from PyQt5.QtWidgets import QWidget

from Frontend.src.ui.edit_window import Ui_Form
from Frontend.src.mplwidget import MplWidget



class EditWindow (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()

        # GRAPHHHHHH
        # crear el box para la toolbar
        self.MplWidget.show_toolbar(self.Toolbar2)