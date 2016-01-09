#!/usr/bin/env python

import sys
import PyQt4
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QApplication,QWidget,QVBoxLayout

__version__ = '0.0.1'

from ui_textinp import Ui_TextInp
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class TextInp(QWidget, Ui_TextInp):
    def __init__(self, parent=None):
        super(TextInp, self).__init__(parent)
        self.setupUi(self)
        vBox = QVBoxLayout()
        vBox.addWidget(self.horizontalLayoutWidget)
        self.setLayout(vBox)
    @QtCore.pyqtSlot()
    def getPressed(self):
        print "PRESSED"
if __name__ == '__main__':
    app = QApplication(sys.argv)
    textinp = TextInp()
    textinp.show()
    sys.exit(app.exec_())
