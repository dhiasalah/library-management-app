from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from PY.ISIMM import ISIMM
from PY.LoginCreate import Login
from PY.MainWindow import MainWindow
import sys
class Main:
    def __init__(self):
        self.isimm=ISIMM()
        self.login=Login(self.isimm)

app=QtWidgets.QApplication(sys.argv)
window=Main()
app.exec_()