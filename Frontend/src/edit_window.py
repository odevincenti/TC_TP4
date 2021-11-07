from PyQt5.QtWidgets import QWidget

from Frontend.src.ui.edit_window import Ui_Form



class EditWindow (QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

        self.setupUi(self)
        self.show()