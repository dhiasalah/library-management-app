from PYConverted.Main_window_picture import Ui_Dialog
from PyQt5.QtWidgets import *

class MainWindowPicture :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm