__author__ = 'kehao'
import sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Hello World", None)
button.show()
app.exec_()